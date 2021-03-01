FROM python:3

RUN pip3 install requests

ADD init.py init.py

ENTRYPOINT ["python3", "init.py"]
