# Dockerfile for microservice1 (Product Catalog)
FROM python:3.9

WORKDIR /app

COPY microservice1 /app

RUN pip install -r requirements.txt

EXPOSE 8001

CMD ["python", "app.py"]
