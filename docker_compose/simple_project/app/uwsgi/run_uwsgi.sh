#!/usr/bin/env bash

set -e
chown www-data:www-data /var/log
python manage.py collectstatic --noinput

# Добавлен код для ожидания доступности базы данных
while ! nc -z $DB_HOST $DB_PORT; do
    echo "Waiting for database to be available..."
    sleep 0.1
done

python manage.py migrate
uwsgi --strict --ini /opt/app/uwsgi/uwsgi.ini