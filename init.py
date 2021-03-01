import requests
import urllib

def urlencode(data):
    return urllib.parse.urlencode(data)


headers = {"Content-Type": "application/json"}
data = """{
    \"index_pattern\": \"kheopsmetrics-*\",
    \"rollup_index\": \"rollup_job_kheopsmetrics\",
    \"cron\": \"34 14 * * * ?\",
    \"groups\": {
      \"date_histogram\": {
        \"calendar_interval\": \"1h\",
        \"field\": \"@timestamp\",
        \"delay\": \"1d\",
        \"time_zone\": \"Europe/Zurich\"
      },
      \"terms\": {
        \"fields\": [
          \"fields.instance.keyword\"
        ]
      }
    },
    \"metrics\": [
      {
        \"field\": \"http.kheopsmetrics.number_of_active_album_capability_tokens\",
        \"metrics\": [
          \"min\",
          \"max\"
        ]
      },
      {
        \"field\": \"http.kheopsmetrics.number_of_active_user_capability_tokens\",
        \"metrics\": [
          \"max\",
          \"min\"
        ]
      },
      {
        \"field\": \"http.kheopsmetrics.number_of_album_capability_tokens\",
        \"metrics\": [
          \"min\",
          \"max\"
        ]
      },
      {
        \"field\": \"http.kheopsmetrics.number_of_capability_tokens\",
        \"metrics\": [
          \"max\",
          \"min\"
        ]
      },
      {
        \"field\": \"http.kheopsmetrics.number_of_fav_albums\",
        \"metrics\": [
          \"min\",
          \"max\"
        ]
      },
      {
        \"field\": \"http.kheopsmetrics.number_of_fav_series\",
        \"metrics\": [
          \"max\",
          \"min\"
        ]
      },
      {
        \"field\": \"http.kheopsmetrics.number_of_instances\",
        \"metrics\": [
          \"max\",
          \"min\"
        ]
      },
      {
        \"field\": \"http.kheopsmetrics.number_of_inactive_album_capability_tokens\",
        \"metrics\": [
          \"min\",
          \"max\"
        ]
      },
      {
        \"field\": \"http.kheopsmetrics.number_of_albums\",
        \"metrics\": [
          \"max\",
          \"min\"
        ]
      },
      {
        \"field\": \"http.kheopsmetrics.number_of_inactive_user_capability_tokens\",
        \"metrics\": [
          \"min\",
          \"max\"
        ]
      },
      {
        \"field\": \"http.kheopsmetrics.number_of_orphan_series\",
        \"metrics\": [
          \"min\",
          \"max\"
        ]
      },
      {
        \"field\": \"http.kheopsmetrics.number_of_private_study_comments\",
        \"metrics\": [
          \"max\",
          \"min\"
        ]
      },
      {
        \"field\": \"http.kheopsmetrics.number_of_public_study_comments\",
        \"metrics\": [
          \"max\",
          \"min\"
        ]
      },
      {
        \"field\": \"http.kheopsmetrics.number_of_report_providers\",
        \"metrics\": [
          \"min\",
          \"max\"
        ]
      },
      {
        \"field\": \"http.kheopsmetrics.number_of_series\",
        \"metrics\": [
          \"max\",
          \"min\"
        ]
      },
      {
        \"field\": \"http.kheopsmetrics.number_of_studies\",
        \"metrics\": [
          \"min\",
          \"max\"
        ]
      },
      {
        \"field\": \"http.kheopsmetrics.number_of_study_comments\",
        \"metrics\": [
          \"max\",
          \"min\"
        ]
      },
      {
        \"field\": \"http.kheopsmetrics.number_of_unpopulated_series\",
        \"metrics\": [
          \"min\",
          \"max\"
        ]
      },
      {
        \"field\": \"http.kheopsmetrics.number_of_unpopulated_studies\",
        \"metrics\": [
          \"max\",
          \"min\"
        ]
      },
      {
        \"field\": \"http.kheopsmetrics.number_of_users\",
        \"metrics\": [
          \"min\",
          \"max\"
        ]
      },
      {
        \"field\": \"http.kheopsmetrics.number_of_user_capability_tokens\",
        \"metrics\": [
          \"max\",
          \"min\"
        ]
      }
    ],
    \"timeout\": \"20s\",
    \"page_size\": 1000
}"""
response = requests.post("http://elasticsearch:9200/_rollup/job/rollup_job_kheops_metrics222", headers=headers, data=urlencode(data))
print(response.status_code)




response = requests.post("http://elasticsearch:9200/_rollup/job/rollup_job_kheops_metrics/_start")
print(response.status_code)
