FROM python:3.9-alpine
MAINTAINER BobRooney

ENV PYTHONUNBUFFERED 1

# install dependencies
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

# setup folder structure
RUN mkdir /app
WORKDIR /app
COPY ./app /app

# setup nonroot user
RUN adduser -D user
USER user
