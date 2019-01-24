#!/bin/bash

echo type in "start" or "stop" to control the application stack
read input

if [[ $input == "start"]]; then
    echo starting docker
    docker-compose up -d
fi
if [[ $input == "stop"]]; then
    echo stoping docker
    docker-compose down
fi
