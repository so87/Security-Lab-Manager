#!/bin/bash

function usage(){
   echo "usage: ./$0 <start|stop> <dev|prod>"
   exit 1 
}

if [ "$#" -ne 2 ]; then
    usage
fi

if [[ $1 == "start" ]]; then
    echo starting docker
    if [[ $2 == "dev" ]]; then
        export RUN_ENV="bash -c 'sh deploy_dev.sh && sh start-django.sh'"
        docker-compose up
    elif [[ $2 == "prod" ]]; then
        export RUN_ENV="bash -c 'sh deploy_prod.sh && sh start-django.sh'"
        docker-compose up
    else
        usage
    fi
elif [[ $1 == "stop" ]]; then
    echo stoping docker
    docker-compose down
fi