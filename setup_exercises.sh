#!/bin/sh

export RUN_ENV="bash -c 'sh deploy_dev.sh && sh start-django.sh'"
docker-compose up -d
sleep 5s
docker-compose exec web-django python manage.py shell -c "from slmApp.models import Settings; Settings.objects.create(name='instance1',hostname='localhost',ram='4000', cores='3', instances='1')"
docker-compose exec web-django python manage.py shell -c "from slmApp.models import Exercises; Exercises.objects.create(name='XSS 1',description = 'Bypass the HTML input filter. An admin is trying to login every 30seconds')"
docker-compose exec web-django python manage.py shell -c "from slmApp.models import Exercises; Exercises.objects.create(name='Weak Auth 1',description = 'The login page is broken! Find out how to get the secret key!')"
docker-compose exec web-django python manage.py shell -c "from slmApp.models import Exercises; Exercises.objects.create(name='Weak Auth 2',description = 'How does the login page work?')"
docker-compose exec web-django python manage.py shell -c "from slmApp.models import Exercises; Exercises.objects.create(name='Weak Auth 3',description = 'You might be able to execute some privileged actions')"
docker-compose exec web-django python manage.py shell -c "from slmApp.models import Exercises; Exercises.objects.create(name='C_Weak Auth 1',description = 'The C application has hard coded username and password')"
docker-compose down