#!/usr/bin/env bash
# exit on error
set -o errexit

echo "Installing requirements"
pip install -r requirements.txt

echo "Collecting static files"
python manage.py collectstatic --no-input

echo "Making migrations"
python manage.py makemigrations

echo "Migrating to database"
python manage.py migrate

echo "Creating super user"
python manage.py create_superuser

echo "Successfully ran build script"
