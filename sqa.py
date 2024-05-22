import json
from torch.utils.data import Dataset
from PIL import Image
from transformers import InstructBlipProcessor
from skill_plans import plans

model = "instructblip-flan-t5-xxl"
processor = InstructBlipProcessor.from_pretrained(f"Salesforce/{model}")
max_length = 256

class sqa_dataset(Dataset):
    def __init__(self, split):
        self.split = split
        self.dataset = json.load(open(f"sqa_data/problems_merge.json", "r"))

    def __len__(self):
        return len(self.dataset)

    def __getitem__(self, idx):
        problem = self.dataset.iloc[idx]
        p = self.dataset.iloc[idx]['puzzle_num']
        text = f"<Image> Question: {problem['Question']} Options: (a) {problem['A']} (b) {problem['B']} (c) {problem['C']} (d) {problem['D']} (e) {problem['E']}. Answer:"
        image = Image.open(f"data/{self.split}_data/{p}/{problem['image']}").convert("RGB")
        label = f"({problem['Answer']})".lower()
        input = processor(images=image, text=text, return_tensors="pt", padding="max_length", truncation=True, max_length=max_length)
        output = processor.tokenizer(text=label, return_tensors="pt", padding="max_length", truncation=True, max_length=4)
        input["labels"] = output.input_ids
        for x in input:
            input[x] = input[x][0]
        return input

class sqa_dataset_with_plans(sqa_dataset):
    def __init__(self, split):
        super().__init__(split)
        self.context = hints

    def __getitem__(self, idx):
        problem = self.dataset.iloc[idx]
        puzzle_num = self.dataset.iloc[idx]['puzzle_num']
        p = self.dataset.iloc[idx]['puzzle_num']
        text = f"<Image> Hint: {hints[puzzle_num-1]} Question: {problem['Question']} Options: (a) {problem['A']} (b) {problem['B']} (c) {problem['C']} (d) {problem['D']} (e) {problem['E']}. Answer:"
        image = Image.open(f"data/{self.split}_data/{p}/{problem['image']}").convert("RGB")
        label = f"({problem['Answer']})".lower()
        input = processor(images=image, text=text, return_tensors="pt", padding="max_length", truncation=True, max_length=max_length)
        output = processor.tokenizer(text=label, return_tensors="pt", padding="max_length", truncation=True, max_length=4)
        input["labels"] = output.input_ids
        for x in input:
            input[x] = input[x][0]
        return input
