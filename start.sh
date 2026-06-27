#!/bin/bash
python manage.py migrate --noinput
gunicorn beckend.wsgi:application --bind 0.0.0.0:$PORT --workers 4
