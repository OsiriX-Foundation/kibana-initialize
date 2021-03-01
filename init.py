import requests

response = requests.post("http://elasticsearch:9200/_rollup/job/rollup_job_kheops_metrics/_start")
print(response.status_code)
