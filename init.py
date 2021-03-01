import requests
import urllib

def urlencode(data):
    return urllib.parse.urlencode(data)


headers = {"Content-Type": "application/json"}
response = requests.put("http://elasticsearch:9200/_rollup/job/rollup_job_kheops_metrics222", headers=headers, data=open("rollup_job_kheops_metrics.json", "rb"))
print(response.status_code)
print(response.content)




response = requests.post("http://elasticsearch:9200/_rollup/job/rollup_job_kheops_metrics/_start")
print(response.status_code)
print(response.content)
