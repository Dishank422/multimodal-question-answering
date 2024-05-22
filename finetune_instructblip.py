from torch.utils.data import DataLoader
from smart import smart_dataset, smart_dataset_with_human_prompts
from peft import LoraConfig, get_peft_model
import torch
from tqdm import tqdm
from accelerate import Accelerator
from transformers import (
    InstructBlipProcessor,
    InstructBlipForConditionalGeneration,
    BitsAndBytesConfig,
)

human_prompts = True
model = "instructblip-flan-t5-xxl"
processor = InstructBlipProcessor.from_pretrained(f"Salesforce/{model}")
allowed_tokens = ["(", ")", "a", "b", "c", "d", "e"]
allowed_token_ids = torch.tensor(processor.tokenizer.convert_tokens_to_ids(allowed_tokens), device="cuda")

def constrained_decode(logits):
    max_vals = torch.index_select(logits, -1, allowed_token_ids)
    max_index = torch.argmax(max_vals, dim=-1)
    decoded_tokens = allowed_token_ids[max_index]
    return decoded_tokens

batch_size = 4
if human_prompts:
    train_dataset = smart_dataset_with_human_prompts("train")
    val_dataset = smart_dataset_with_human_prompts("val")
else:
    train_dataset = smart_dataset("train")
    val_dataset = smart_dataset("val")

train_dataloader = DataLoader(train_dataset, shuffle=True, batch_size=batch_size, num_workers=12)
val_dataloader = DataLoader(val_dataset, batch_size=batch_size, num_workers=12)

bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_use_double_quant=True,
    bnb_4bit_compute_dtype=torch.float16,
)

vision_layers = ["qkv", "fc1", "fc2", "projection"]
qformer_layers = ["query", "key", "value", "dense"]

model = InstructBlipForConditionalGeneration.from_pretrained(f"Salesforce/{model}", quantization_config=bnb_config, device_map="auto")
config = LoraConfig(
    r=16,
    lora_alpha=32,
    lora_dropout=0.05,
    bias="none",
    target_modules=qformer_layers
)

model = get_peft_model(model, config)
model.print_trainable_parameters()

optimizer = torch.optim.AdamW(model.parameters(), lr=3e-5)

accelerator = Accelerator()
model, optimizer, train_dataloader, val_dataloader = accelerator.prepare(model, optimizer, train_dataloader, val_dataloader)

max_val_acc = 0
for epoch in range(20):
    print("-"*40, "\nTraining\n", "-"*40, "\n")
    model.train()
    pbar = tqdm(train_dataloader, desc=f"Train Epoch {epoch}")
    train_acc = 0
    for batch in pbar:
        labels = batch.pop("labels")
        outputs = model(**batch, labels=labels)

        loss = outputs.loss
        accelerator.backward(loss)

        optimizer.step()
        optimizer.zero_grad()

        preds = torch.argmax(outputs["logits"], dim=-1)
        #preds = constrained_decode(outputs["logits"])
        preds = processor.batch_decode(preds, skip_special_tokens=True)
        labels_text = processor.batch_decode(labels, skip_special_tokens=True)
        acc = sum([preds[i][-2]==labels_text[i][-2] for i in range(batch_size)])/batch_size
        train_acc += acc

        pbar.set_postfix({"loss": loss.item(), "acc": acc})

    print("-" * 40, "\nValidation\n", "-" * 40, "\n")
    model.eval()
    pbar = tqdm(val_dataloader, desc=f"Val Epoch {epoch}")
    val_acc = 0
    with torch.no_grad():
        for batch in pbar:
            labels = batch.pop("labels")

            outputs = model(**batch, labels=labels)

            loss = outputs.loss

            preds = torch.argmax(outputs["logits"], dim=-1)
            #preds = constrained_decode(outputs["logits"])
            preds = processor.batch_decode(preds, skip_special_tokens=True)
            labels_text = processor.batch_decode(labels, skip_special_tokens=True)
            acc = sum([preds[i][-2] == labels_text[i][-2] for i in range(batch_size)]) / batch_size
            val_acc += acc

            pbar.set_postfix({"loss": loss.item(), "acc": acc})

    train_acc /= len(train_dataloader)
    val_acc /= len(val_dataloader)
    print(f"Train accuracy epoch: {train_acc}")
    print(f"Val accuracy epoch: {val_acc}")

    if val_acc > max_val_acc:
        max_val_acc = val_acc
        model.save_pretrained("result/model8/")
