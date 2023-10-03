FROM python:3.11.4

ENV PYTHONUNBUFFERED=1
WORKDIR /instagram
COPY requirements.txt /instagram
RUN pip3 install -r requirements.txt