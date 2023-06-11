FROM python:3.8

COPY ./requirements.txt /requirements.txt
RUN pip install --upgrade pip
RUN pip install pip-tools
RUN pip install -r requirements.txt

WORKDIR /code
COPY . /code/
