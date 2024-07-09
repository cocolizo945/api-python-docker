
FROM python:3.7-alpine

WORKDIR /appflask

ENV FLASK_APP app.py

ENV FLASK_RUN_HOST 0.0.0.0

RUN apk add g++
RUN apk add --no-cache zlib-dev gcc musl-dev jpeg-dev linux-headers

COPY requirements.txt requirements.txt


RUN pip3 install numpy
RUN pip3 install Pillow

RUN pip3 --no-cache-dir install -r requirements.txt

COPY . /appflask