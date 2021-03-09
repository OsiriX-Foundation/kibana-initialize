import requests
import urllib
import time
import functools

print = functools.partial(print, flush=True)

#print("waiting 3 min before executing the script")
#time.sleep(3 * 60)
#print("start script")

while True:
    try:
        response = requests.get("http://elasticsearch:9200/_cluster/health?wait_for_status=yellow&timeout=10s")
        print(response.status_code)
        if response.status_code == 200:
            break
        else:
            time.sleep(10)
    except:
        time.sleep(10)
        print("exception!")


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
            break
        else:
            time.sleep(10)
    except:
        time.sleep(10)
        print("exception!")


print("End of the script")
