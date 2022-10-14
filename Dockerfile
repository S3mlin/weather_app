FROM python:slim

RUN useradd weather_app

WORKDIR /home/weather_app

COPY requirements.txt requirements.txt
RUN python -m venv weather_app_venv
RUN weather_app_venv/bin/pip install -r requirements.txt
RUN weather_app_venv/bin/pip install gunicorn pymysql cryptography

COPY app app
COPY microblog.py config.py boot.sh ./
RUN chmod a+x boot.sh

ENV FLASK_APP weather_app.py

RUN chown -R weather_app:weather_app ./
USER weather_app

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]