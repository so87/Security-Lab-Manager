#!/bin/sh

if [ "$#" -ne 4 ]; then
    echo "usage: ./$0 exercise_name user port up|down"
    exit 1
fi

export container_port=$3
export container_name=$1$2

if [ "$4" = "up" ]; then
    docker-compose -p $container_name -f $1.yml $4 -d
else
    docker-compose -p $container_name -f $1.yml $4
fi