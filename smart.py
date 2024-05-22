import pandas as pd
from torch.utils.data import Dataset
from PIL import Image
from transformers import InstructBlipProcessor
from puzzle_hints import hints

model = "instructblip-flan-t5-xxl"
processor = InstructBlipProcessor.from_pretrained(f"Salesforce/{model}")
max_length = 256

class smart_dataset(Dataset):
    def __init__(self, split):
        self.split = split
        csv_list = []
        for i in range(1, 102):
            data = pd.read_csv(f"data/{self.split}_data/{i}/puzzle_{i}.csv", header=0)
            data["puzzle_num"] = [i]*len(data)
            data.drop("id", axis=1, inplace=True)
            csv_list.append(data)
        self.dataset = pd.concat(csv_list, ignore_index=True)
        self.dataset.drop("Note", axis=1, inplace=True)

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

class smart_dataset_with_human_prompts(smart_dataset):
    def __init__(self, split):
        super().__init__(split)
        self.context = hints

    def __getitem__(self, idx):
        problem = self.dataset.iloc[idx]
        puzzle_num = self.dataset.iloc[idx]['puzzle_num']
        p = self.dataset.iloc[idx]['puzzle_num']
        text = f"<Image> Question: {problem['Question']} Options: (a) {problem['A']} (b) {problem['B']} (c) {problem['C']} (d) {problem['D']} (e) {problem['E']}. Answer:"
        image = Image.open(f"data/{self.split}_data/{p}/{problem['image']}").convert("RGB")
        label = f"{hints[puzzle_num-1]} Answer: ({problem['Answer']})".lower()
        #input = processor(images=image, text=text, return_tensors="pt")
        input = processor(images=image, text=text, return_tensors="pt", padding="max_length", truncation=True, max_length=170)
        #output = processor.tokenizer(text=label, return_tensors="pt")
        output = processor.tokenizer(text=label, return_tensors="pt", padding="max_length", truncation=True, max_length=150)
        input["labels"] = output.input_ids
        for x in input:
            input[x] = input[x][0]
        return input