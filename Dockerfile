# Specify the base image
FROM python:3.10.6-slim-buster

# Set the working directory inside the container
WORKDIR /canine_classifier

# Copy the application code to the container
COPY snoop_dog snoop_dog
COPY models models
COPY data data

# Install the required dependencies
COPY setup.py setup.py
COPY requirements.txt requirements.txt
RUN pip install .

# Define the command to run your API
CMD uvicorn snoop_dog.api.api:app --host 0.0.0.0 --port $PORT
