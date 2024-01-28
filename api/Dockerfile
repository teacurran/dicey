FROM python:3.9

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

ENTRYPOINT ["./boot.sh"]
