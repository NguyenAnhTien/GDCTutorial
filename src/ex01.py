"""
"""
import requests
import json

fields = [
    "file_name",
    "file_id",
    "file_size",
    "access",
    "data_category",
    "cases.submitter_id",
    "cases.samples.sample_type",
    "cases.disease_type",
    "cases.project.project_id",
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
            "value": ["breast"]
            }
        },
        {
        "op": "in",
        "content":{
            "field": "files.data_category",
            "value": ["transcriptome profiling"]
            }
        },
        {
        "op": "in",
        "content":{
            "field": "files.data_format",
            "value": ["TSV"]
            }
        }
    ]
}

# A POST is used, so the filter parameters can be passed directly as a Dict object.
params = {
    "filters": filters,
    "fields": fields,
    "size": "200000"
    }

# The parameters are passed to 'json' rather than 'params' in this case
response = requests.post(files_endpt, headers = {"Content-Type": "application/json"}, json = params)

result = response.content.decode("utf-8")
result = json.loads(result)
with open('output.json', 'w') as file:
    json.dump(result, file, indent=4)

