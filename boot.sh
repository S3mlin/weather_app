#!/bin/bash
source weather_app_venv/bin/activate
exec gunicorn -b :8080 --access-logfile - --error-logfile - weather_app:app