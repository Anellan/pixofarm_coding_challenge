FROM python:3.9.1-slim

COPY requirements.txt /app/requirements.txt
WORKDIR /app/

RUN pip install -r requirements.txt

COPY ./app /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH=/app
