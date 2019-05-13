FROM python:3.6.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /TODO
WORKDIR /TODO
COPY requirements.txt /TODO/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /TODO/