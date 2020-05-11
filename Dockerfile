FROM alpine:3.11
MAINTAINER hchan@alauda.io

RUN apk --no-cache --update add python3 vim curl sshpass python3-dev gcc musl-dev openldap-dev openssh chromium-chromedriver chromium

COPY requirements.txt .
RUN pip3 install --upgrade pip && pip3 install -r /requirements.txt

WORKDIR /app
COPY . /app
#RUN curl -LO https://npm.taobao.org/mirrors/chromedriver/2.44/chromedriver_linux64.zip && unzip chromedriver_linux64.zip && chmod +x chromedriver && mv chromedriver /usr/local/bin/

