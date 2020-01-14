FROM python:3.7.6-alpine3.10


ENV http_proxy=http://10.40.14.55:8080
ENV https_proxy=http://10.40.14.55:8080

ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt

ENV http_proxy=
ENV https_proxy=
CMD python app.py