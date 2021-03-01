FROM python:3

RUN pip3 install requests && \
    pip3 install urllib3

ADD init.py init.py
ADD rollup_job_kheops_metrics.json rollup_job_kheops_metrics.json

ENTRYPOINT ["python3", "init.py"]
