FROM python:3.12.8

COPY . /opt/sensor_api/
WORKDIR /opt/sensor_api

RUN pip install -r requirements.txt

EXPOSE 5000/tcp

CMD ["gunicorn", "-c", "python:config.gunicorn", "app.app:create_app()"]
