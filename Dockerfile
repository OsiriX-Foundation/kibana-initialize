FROM python:3

ADD init.py init.py

ENTRYPOINT ["python3", "init.py"]
