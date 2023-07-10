import requests
import json

fields = [
    "file_name",
    "file_id",
    "file_size",
    "access",
    "cases.case_id",
    "cases.diagnoses.primary_diagnosis",
    "cases.diagnoses.prior_malignancy",
    "cases.diagnoses.treatments.treatment_or_therapy",
    "cases.diagnoses.classification_of_tumor",
    "cases.diagnoses.days_to_recurrence",
    "cases.diagnoses.days_to_death",
    "cases.diagnoses.progression_or_recurrence",
    "cases.diagnoses.tumor_grade",
    "cases.diagnoses.tumor_stage",
    "data_category",
    "cases.submitter_id",
    "cases.samples.sample_type",
    "cases.disease_type",
    "cases.project.project_id",
    "cases.samples.portions.slides.percent_tumor_cells",
    "cases.samples.portions.slides.percent_tumor_nuclei",
    "cases.samples.tumor_descriptor",
]

fields = ",".join(fields)

files_endpt = "https://api.gdc.cancer.gov/files"

# This set of filters is nested under an 'and' operator.
filters = {
    "op": "and",
    "content":[
        {
        "op": "in",
        "content":{
            "field": "cases.project.primary_site",
            "value": ["Lung"]
            }
        },
        {
        "op": "in",
        "content":{
            "field": "files.experimental_strategy",
            "value": ["miRNA-Seq"]
            }
        },
        {
        "op": "in",
        "content":{
            "field": "cases.samples.sample_type",
            "value": ["primary tumor", "solid tissue normal"]
            }
        },
        {
        "op": "in",
        "content":{
            "field": "files.access",
            "value": ["open"]
            }
        }
    ]
}

# A POST is used, so the filter parameters can be passed directly as a Dict object.
params = {
    "filters": filters,
    "fields": fields,
    "size": "2000000"
    }

# The parameters are passed to 'json' rather than 'params' in this case
response = requests.post(files_endpt, headers = {"Content-Type": "application/json"}, json = params)

result = response.content.decode("utf-8")
result = json.loads(result)

values = {
    "primary_diagnosis": set(),
    "prior_malignancy": set(),
    "treatment_or_therapy": set(),
    "classification_of_tumor": set(),
    "days_to_recurrence": set(),
    "progression_or_recurrence": set(),
    "sample_type": set(),
    "disease_type": set(),
    "tumor_grade" : set(),
    "tumor_stage" : set(),
    "tumor_descriptor" : set(),
    "project_id" : set(),
}

def walk(node):
    for key, item in node.items():
        if isinstance(item, dict):
            walk(item)
        elif isinstance(item, list):
            for el in item:
                walk(el)
        else:
            if key in values:
                values[key].add(item)

with open("ex04.json", "w") as f:
    json.dump(result, f, indent=4)

results = result["data"]["hits"]
for result in results:
    walk(result)


for key, value in values.items():
    values[key] = list(value)
print(json.dumps(values, indent=4))
#print("#case id: ", len(values["case_id"]))
