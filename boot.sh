#!/bin/sh

echo "Starting API"
while ! nc -z $REDIS_HOST 5432; do
  sleep 0.1
done

echo "Connected to Postgres"
export FLASK_APP=src/api.py

exec gunicorn --bind 0.0.0.0:5005 wsgi:app \
  --access-logfile=- \
  --timeout 3000 \
  --worker-tmp-dir=/dev/shm \
  --workers=2 \
  --threads=2 \
  --worker-class=gthread \
  --log-file=- \
  --max-requests 5000 \
  --max-requests-jitter 100
