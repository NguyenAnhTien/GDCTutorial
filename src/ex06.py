"""
"""
import json


with open('ex04.json') as f:
    data = json.load(f)

samples = []
data = data["data"]["hits"]

for case in data:
    cases = case["cases"]
    for case in cases:
        samples.append(
            {
                "case_id": case["case_id"],
                "project_id": case["project"]["project_id"],
                "sample_type": case["samples"][0]["sample_type"],
            }
        )

pos = 0
neg = 0
for sample in samples:
    if sample["sample_type"] == "Primary Tumor":
        pos += 1
    else:
        neg += 1
print(pos, neg)
