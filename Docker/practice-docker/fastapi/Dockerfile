FROM python:3.8.5

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

RUN pip install fastapi uvicorn pymysql python-decouple cryptography

COPY . /usr/src/app/

EXPOSE 8000

CMD uvicorn main:app --host 0.0.0.0 --port 8000 --reload
