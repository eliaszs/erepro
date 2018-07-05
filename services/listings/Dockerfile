FROM python:slim

RUN apt-get update -y && apt-get install -y git

WORKDIR /app

COPY ./requirements.txt ./requirements.txt
RUN pip install -r ./requirements.txt
COPY . .

CMD python main.py
