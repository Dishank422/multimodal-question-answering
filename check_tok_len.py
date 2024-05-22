from smart import smart_dataset_with_human_prompts
from tqdm import tqdm
dic = [0]*1000
dic2 = [0]*1000
d = smart_dataset_with_human_prompts("val")
for i in tqdm(range(len(d))):
    dic[len(d[i]["labels"])] += 1
    dic2[len(d[i]["input_ids"])] += 1

print("labels")
for index, val in enumerate(dic):
    if val != 0:
        print(index, val)

print("input_ids")
for index, val in enumerate(dic2):
    if val != 0:
        print(index, val)
