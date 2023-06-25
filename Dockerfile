FROM python:3.10

COPY ./requirements.txt /requirements.txt
RUN pip install --upgrade pip
RUN pip install pip-tools
RUN pip install -r requirements.txt

RUN apt update \
    && apt install -v libpq-dev gcc

RUN pip install psycopg2

WORKDIR /code
COPY . /code/
