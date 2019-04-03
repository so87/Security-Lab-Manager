#!/bin/sh

export RUN_ENV="bash -c 'sh deploy_dev.sh && sh start-django.sh'"
docker-compose up -d
docker-compose exec web-django python manage.py shell -c "from slmApp.models import Settings; Settings.objects.create(name='instance1',hostname='localhost',ram='4000', cores='3', instances='1')"
docker-compose exec web-django python manage.py shell -c "from slmApp.models import Exercises; Exercises.objects.create(name='XSS 1',description = 'Bypass the HTML input filter. An admin is trying to login every 30seconds')"
docker-compose down