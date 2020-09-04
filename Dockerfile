FROM python:3.7
ENV PYTHONUNBUFFERD 1

WORKDIR /anonymous_pro
COPY requirements.txt /anonymous_pro/

RUN pip3 install -r requirements.txt
COPY . /anonymous_pro/

EXPOSE 10000