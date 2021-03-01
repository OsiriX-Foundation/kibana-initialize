FROM python:3

RUN pip3 install requests && \
    pip3 install urllib3

ADD init.py init.py

ENTRYPOINT ["python3", "init.py"]
