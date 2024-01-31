FROM python:3.9

ADD https://github.com/ufoscout/docker-compose-wait/releases/download/2.9.0/wait /wait
RUN chmod +x /wait

WORKDIR /usr/src/application

COPY requirements.txt ./
RUN pip install pip-tools==7.3.0
RUN pip-sync requirements.txt

COPY app ./app
COPY migrations ./migrations
COPY config.py application.py boot.sh gunicorn.ini ./

RUN chmod +x ./boot.sh

ENV FLASK_APP=application.py

EXPOSE 8080

CMD ["./boot.sh"]
