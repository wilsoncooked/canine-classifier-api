# Specify the base image
FROM python:3.10.6-buster

# Set the working directory inside the container
WORKDIR /canine_classifier

# Copy the application code to the container
COPY snoop_dog /snoop_dog
COPY models /models

# Install the required dependencies
COPY requirements.txt /requirements.txt
COPY requirements.txt /requirements.txt
RUN pip install --upgrade pip && \
    pip install -r /requirements.txt

CMD uvicorn app.simple:app --host 0.0.0.0 $PORT
