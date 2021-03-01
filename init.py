import requests
import urllib
import time


time.sleep(3 * 60)

print("Create and start rollup_job_kheops_metrics")
response = requests.post("http://elasticsearch:9200/_rollup/job/rollup_job_kheops_metrics/_start")
if response.status_code == 404:
    headers = {"Content-Type": "application/json"}
    response = requests.put("http://elasticsearch:9200/_rollup/job/rollup_job_kheops_metrics", headers=headers, data=open("rollup_job_kheops_metrics.json", "rb"))
    print("Create")
    print(response.status_code)
    print(response.content)

    response = requests.post("http://elasticsearch:9200/_rollup/job/rollup_job_kheops_metrics/_start")
    print("Start")
    print(response.status_code)
    print(response.content) 
else:
    print("rollup_job_kheops_metrics already exist and already started")


    
headers = {"kbn-xsrf": "true"}
files = {'file': open('export.ndjson', 'rb')}
response = requests.post("http://kibana:9200/api/saved_objects/_import" ,files=files)
print(response.status_code)
print(response.content) 
