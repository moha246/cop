#!/usr/bin/env bash
# exit on error
set -o errexit

poetry --version
poetry self update 1.4.0

poetry install

python manage.py collectstatic --no-input
python manage.py makemigrations
python manage.py migrate
