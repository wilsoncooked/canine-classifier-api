# Specify the base image
FROM python:3.8.12-buster

# Set the working directory inside the container
WORKDIR /canine_classifier
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy the application code to the container
COPY snoop_dog snoop_dog
COPY models models

# Install the required dependencies
COPY setup.py setup.py
RUN pip install .

CMD uvicorn snoop_dog.api.api:app --host 0.0.0.0
