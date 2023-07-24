# Use an official Python runtime as a parent image
FROM python:3.8

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install required dependencies
RUN pip install Flask
RUN pip install Flask-WTF
RUN pip install Flask-MySQL

# Set the environment variable for Flask
ENV FLASK_APP=Home.py

# Expose port 80 to the outside world
EXPOSE 80

# Run the Flask application
CMD ["flask", "run", "--host=0.0.0.0", "--port=80"]
