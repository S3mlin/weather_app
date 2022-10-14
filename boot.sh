#!/bin/bash
source weather_app_venv/bin/activate
exec gunicorn -b :5000 --access-logfile - --error-logfile - microblog:app