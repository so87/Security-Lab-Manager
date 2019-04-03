#!/bin/sh

read -p 'Enter your username: ' name
read -p 'Enter your email: ' email
read -p 'Enter your password: ' password

export RUN_ENV="bash -c 'sh deploy_dev.sh && sh start-django.sh'"
docker-compose up -d
docker-compose exec web-django python manage.py shell -c "from slmApp.models import CustomUser; CustomUser.objects.create_superuser('$name', '$email', '$password')" 
docker-compose down