from peft import PeftModel
import torch
from transformers import (
    InstructBlipForConditionalGeneration,
    BitsAndBytesConfig,
    InstructBlipProcessor,
)
from smart import smart_dataset, smart_dataset_with_human_prompts
from torch.utils.data import DataLoader
from pytorch_grad_cam import GradCAMPlusPlus
from pytorch_grad_cam.utils.image import show_cam_on_image
from sklearn import preprocessing as pre
import matplotlib.pyplot as plt
from tqdm import tqdm
import pandas as pd
import warnings
warnings.filterwarnings("error")

human_prompts = True
model = "instructblip-flan-t5-xxl"
batch_size = 1
if human_prompts:
    val_dataset = smart_dataset_with_human_prompts("val")
else:
    val_dataset = smart_dataset("val")
val_dataloader = DataLoader(val_dataset, batch_size=batch_size)

bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_use_double_quant=True,
    bnb_4bit_compute_dtype=torch.float16,
)

processor = InstructBlipProcessor.from_pretrained(f"Salesforce/{model}")
model = InstructBlipForConditionalGeneration.from_pretrained(f"Salesforce/{model}", quantization_config=bnb_config, device_map="auto")

model = PeftModel.from_pretrained(model, "result/model1", is_trainable=True)

target_layers = [model.base_model.model.vision_model.encoder.layers[-1].layer_norm1]

def reshape_transform(tensor, height=16, width=16):
    result = tensor[:, 1 :  , :].reshape(tensor.size(0),
        height, width, tensor.size(2))

    # Bring the channels to the first dimension,
    # like in CNNs.
    result = result.transpose(2, 3).transpose(1, 2)
    return result

cam = GradCAMPlusPlus(model=model, target_layers=target_layers, use_cuda=False, reshape_transform=reshape_transform)
# cam_metric = ROADMostRelevantFirst(percentile=75)

puzzle_type_info = pd.read_csv("data/puzzle_type_info.csv", header=0)
explanation_scores = []
puzzle_type_scores = {x: [] for x in pd.unique(puzzle_type_info.type)}
puzzle_scores = [[] for _ in range(101)]
per_puzzle_answer = {}

count = 0
puzzle = 0
for index, i in tqdm(enumerate(val_dataloader)):
    if index//100 != puzzle:
        continue
    try:
        grayscale_cam = cam(input_tensor=i, targets=i["labels"][:, 1], aug_smooth=True, eigen_smooth=True)

        outputs = model(**i)
        labels = i["labels"]
        preds = torch.argmax(outputs["logits"], dim=-1)
        preds = processor.batch_decode(preds, skip_special_tokens=True)
        labels_text = processor.batch_decode(labels, skip_special_tokens=True)
        acc = sum([preds[i][1] == labels_text[i][1] for i in range(batch_size)]) / batch_size

        grayscale_cam = grayscale_cam[0, :]
        rgb_image = i["pixel_values"][0].permute(1, 2, 0).numpy()
        rgb_image = pre.MinMaxScaler().fit_transform(rgb_image.reshape(-1, 3)).reshape(rgb_image.shape)
        visualization = show_cam_on_image(rgb_image, grayscale_cam, use_rgb=True)
        count += 1
        if count == 30:
            count = 0
            puzzle += 1
        plt.imshow(visualization)
        plt.savefig(f"result/gcpp/{val_dataset.dataset.iloc[index]['image']}")

        # explanation_scores.append(cam_metric(i, grayscale_cam, i["labels"][:, 1], model)[0])
        puzzle_scores[puzzle].append(acc)
        per_puzzle_answer[val_dataset.dataset.iloc[index]['image']] = acc
        puzzle_type_scores[puzzle_type_info.iloc[puzzle]['type']].append(acc)
    except:
        continue

# print("average explanation score:", sum(explanation_scores) / len(explanation_scores))
# print("\n\n")

for i in range(101):
    print(f"average puzzle {i} score:", sum(puzzle_scores[i]) / len(puzzle_scores[i]))
print("\n\n")

print("puzzle answers:", per_puzzle_answer)
print("\n\n")

for i in puzzle_type_scores:
    print(f"average puzzle type {i} score:", sum(puzzle_type_scores[i]) / len(puzzle_type_scores[i]))
