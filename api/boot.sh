#!/bin/bash

# uwsgi --http :8890 --file application.py --gevent 2000 -l 16 -p 1 -L

# exec gunicorn -c gunicorn.ini application:app
exec gunicorn --worker-class eventlet -w 1 -c gunicorn.ini application:app
