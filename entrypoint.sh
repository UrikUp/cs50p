#!/bin/sh
set -e

echo "Running migrations..."
python manage.py migrate --noinput

echo "Creating superuser..."
python manage.py createsuperuser --no-input || true  # || true so it doesn't fail if already exists

echo "Collecting static files..."
python manage.py collectstatic --noinput

exec "$@"
