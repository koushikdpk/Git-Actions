# Dockerfile for microservice2 (User Management)
FROM python:3.9

WORKDIR /app

COPY microservice2 /app

RUN pip install -r requirements.txt

EXPOSE 8002

CMD ["python", "app.py"]
