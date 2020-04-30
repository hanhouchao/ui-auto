FROM alpine:3.11
MAINTAINER hchan@alauda.io

RUN apk --no-cache --update add python3 vim curl sshpass python3-dev gcc musl-dev openldap-dev openssh

COPY requirements.txt .
RUN pip3 install --upgrade pip && pip3 install -r /requirements.txt

WORKDIR /app
COPY . /app

CMD ["/app/docker-run-cmd.sh"]
