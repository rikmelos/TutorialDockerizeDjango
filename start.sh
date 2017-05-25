#!/bin/bash
# -*- ENCODING: UTF-8 -*-
docker-compose build
docker-compose run restapi /usr/local/bin/python manage.py makemigrations
docker-compose run restapi /usr/local/bin/python manage.py migrate
docker-compose up -d
exit
