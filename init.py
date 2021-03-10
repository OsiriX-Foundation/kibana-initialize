import requests
import urllib
import time
import functools
import json

print = functools.partial(print, flush=True)

#print("waiting 3 min before executing the script")
#time.sleep(3 * 60)
#print("start script")

while True:
    try:
        response = requests.get("http://elasticsearch:9200/_cluster/health?wait_for_status=yellow&timeout=30s")
        print(response.status_code)
        if response.status_code == 200:
            print("Elasticsearch is ready")
            break
        else:
            time.sleep(10)
    except:
        print("Elasticsearch is not ready yet")
        time.sleep(10)

   
print("import kinana saved objects")

headers = {"kbn-xsrf": "true"}
params={'overwrite': 'true'}
files = {'file': open('export.ndjson', 'rb')}
while True:
    try:
        response = requests.post("http://kibana:5601/api/saved_objects/_import", params=params, files=files, headers=headers)
        print(response.status_code)
        print(response.content) 
        if response.status_code == 200:
            json_object = json.load(response.content)
            if json_object["successCount"] != 0
                break
            else:
                time.sleep(10)
        else:
            time.sleep(10)
    except:
        print("Kibana is not ready yet")
        time.sleep(10)


print("Create and start rollup_job_kheops_metrics")
response = requests.post("http://elasticsearch:9200/_rollup/job/rollup_job_kheops_metrics/_start")
if response.status_code == 404:
    headers = {"Content-Type": "application/json"}
    while True:
        response = requests.put("http://elasticsearch:9200/_rollup/job/rollup_job_kheops_metrics", headers=headers, data=open("rollup_job_kheops_metrics.json", "rb"))
        print(response.status_code)
        print(response.content)
        if response.status_code == 200:
            print("Create")
            break
        else:
            time.sleep(10)
    while True:
        response = requests.post("http://elasticsearch:9200/_rollup/job/rollup_job_kheops_metrics/_start")
        print(response.status_code)
        print(response.content)
        if response.status_code == 200:
            print("Start")
            break
        else:
            time.sleep(10)
else:
    print("rollup_job_kheops_metrics already exist and already started")

        
print("End of the script")
