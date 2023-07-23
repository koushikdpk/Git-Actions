# Dockerfile for microservice4 (Frontend)
FROM python:3.9

WORKDIR /app

COPY frontend /app

RUN pip install -r requirements.txt

EXPOSE 8004

CMD ["python", "app.py"]
