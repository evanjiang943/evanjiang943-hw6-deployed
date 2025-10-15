#!/bin/bash

# Run database migrations
python manage.py migrate --noinput

# Collect static files
python manage.py collectstatic --noinput

# Start gunicorn server
gunicorn assignment_creator.wsgi --log-file -

