release: python manage.py migrate --noinput
web: gunicorn beckend.wsgi:application --bind 0.0.0.0:$PORT --workers 4
