#!/bin/bash

python city_management/manage.py makemigrations -v 3
python city_management/manage.py migrate
python city_management/manage.py migrate event_management
python city_management/manage.py runserver 0.0.0.0:8000