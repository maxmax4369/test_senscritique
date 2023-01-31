# Filename: Dockerfile
FROM python:3.9.6-alpine3.13
WORKDIR /flask_app
COPY . /flask_app
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
