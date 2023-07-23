# Dockerfile for microservice3 (Order Management)
FROM python:3.9

WORKDIR /app

COPY microservice3 /app

RUN pip install -r requirements.txt

EXPOSE 8003

CMD ["python", "app.py"]
