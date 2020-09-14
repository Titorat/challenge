#!/bin/sh

python3 manage.py collectstatic --noinput
python3 manage.py makemigrations
python3 manage.py makemigrations API
python3 manage.py migrate

echo "Running command '$*'"
exec /bin/bash -c "$*"
