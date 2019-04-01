#!/bin/sh
python /code/manage.py makemigrations slmApp
python /code/manage.py migrate
python /code/manage.py runserver 0.0.0.0:8080