# Use a smaller and specialized base image
FROM python:3

# Set the working directory inside the container
WORKDIR /app

# Install required packages
RUN pip install flask flask-wtf flask-mysql

# Copy the application files into the container
COPY . /app

# Create and activate a virtual environment
RUN python -m venv venv
RUN . venv/bin/activate

# Install Python dependencies in the virtual environment
RUN pip install -r requirements.txt

# Expose the port on which Flask will run
EXPOSE 5000

# Run the Flask application
CMD [ "flask", "run", "--host=0.0.0.0" ]
