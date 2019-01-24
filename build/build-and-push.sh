#!/bin/bash

# Versions of contaienrs being used to store on docker hub
docker login
django=python:3
postgresql=postgres:11.1-alpine
nginx=nginx:latest

# django container build
target="simonowens157/django:v1.0"
docker build . -t "$target" -f DockerfileDjango --build-arg django=$django
docker push "$target"

# database container build
target="simonowens157/postgresql:v1.0"
docker build . -t "$target" -f DockerfilePostgresql --build-arg postgresql=$postgresql
docker push "$target"

# proxy container build
target="simonowens157/$nginx"
docker build . -t "$target" -f DockerfileNginx --build-arg nginx=$nginx
docker push "$target"