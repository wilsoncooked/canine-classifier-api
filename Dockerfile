# Specify the base image
FROM python:3.10.6-buster

# Set the working directory inside the container
WORKDIR /canine_classifier

# Copy the application code to the container
COPY canine_classifier /canine_classifier

# Install the required dependencies
COPY requirements.txt /requirements.txt
RUN pip install --upgrade pip
RUN pip install -r /requirements.txt

# CMD uvicorn api.simple:app --host 0.0.0.0 --port $PORT
