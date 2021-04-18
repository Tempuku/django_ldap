#!/usr/bin/env sh

python3 manage.py migrate
python3 manage.py collectstatic --noinput
gunicorn --forwarded-allow-ips=* --bind 0.0.0.0:8080 -w 2 app.wsgi:application
#daphne -b 0.0.0.0 -p 8080 app.asgi:application
