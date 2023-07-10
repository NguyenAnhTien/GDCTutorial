import json

datetimes = {}

with open('ex04.json') as f:
    result = json.load(f)

def walk(node, percent):
    for key, item in node.items():
        if isinstance(item, dict):
            print("heheheheh1")
            walk(item, percent)
        elif isinstance(item, list):
            print("heheheheh2")
            for el in item:
                walk(el, percent)
        else:
            print("heheheheh3")
            print(key)
            if key == 'percent_tumor_cells':
                #print(item)
                return percent.append(item)

for sample in result["data"]["hits"]:
    datetime = sample['created_datetime']
    for case in sample['cases']:
        case_id = case['case_id']
        if case_id == '84c3ba70-afa7-4b69-be69-7ec8d6022c56':
            print(json.dumps(case, indent=4))

for key, value in datetimes.items():
    if key == 'fd9ee494-65fe-4de4-adff-7952a059b17f':
        print(value)
