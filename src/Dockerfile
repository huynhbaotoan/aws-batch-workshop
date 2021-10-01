FROM python:3.6.10
COPY job.py job.py
COPY requirements.txt requirements.txt
COPY config.ini config.ini
RUN pip install -r requirements.txt
CMD ["python", "job.py"]
