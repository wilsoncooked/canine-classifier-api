## Canine Classifier
# Your Dog's DNA in a Snap

# Introduction:
Provide an overview of the backend repository's purpose and functionality.
Mention the technologies used, such as deep learning frameworks, web frameworks, deployment tools, etc.
Our aim in this project is to develop the computer vision, a convolution neural network (deep learning method) based framework to classify the image of dogs. For this purpose, we used Stanford Dog dataset (cropped and processed) from Kaggel ![dataset](https://www.kaggle.com/datasets/miljan/stanford-dogs-dataset-traintest). We used pre-trained models first compared with different CNN architecture families (e.g. VGG, DenseNet, EffienceNet). Since EfficientNet family models gave better accuracy with less computational intense processing, we used EfficientNetV2S for further framework development. A python packaged was developed and together with optimized model, we containerized them in the docker and deployed them in GCP Artigact Registry. FastAPI and Uvicorn were used for server hosting and production API was developed which can be used for the UI/frontend development.

# Installation:
Include step-by-step instructions for setting up the backend environment.
List any dependencies and versions required.
virtualenv "dogenv" was created for this project.
Using setuptools, "snoop_dog" package (v0.0.1) was developed.
We used tensorflow==2.15.0. It is compatible with Apple M chips ('darwin' and 'ARM') and Ubuntu and Windows Intel chips.

# Usage:
EfficientNetV2S pre-trained model was used.
Provide examples of how to use the backend APIs or services.

# Models:
Describe each model included in the repository.
Provide details such as input/output dimensions, architecture, and training data.
Training dataset is the Stanford Dog dataset (cropped and processed) from Kaggel ![dataset](https://www.kaggle.com/datasets/miljan/stanford-dogs-dataset-traintest).
In the EfficientNetV2 pre-trained model, "imagenet" weights, 500 neurons and "relu" activation was used in the dense leyer. In the prediction leyer, 120 neurons and "softmax" activation was used. Gradcam feature was added in the last leyer.
Loss measured by "categorical_crossentropy", "adam" optimizer and "accuracy" for evaluation metrix were used. Other parameters include patience = 3, batchsize = 32 and epochs = 100.

# Deployment:
Explain how to deploy the backend services or models.
Include instructions for setting up servers, containers, or cloud services.
For deployment, Docker image "python:3.10.6-buster" was used as base image for python. Docker containers were deployed locally first and then in the Google cloud platform (Artifact Registry). 4Gb capacity was assigned for Docker image to run.

# API Documentation:
Document all available API endpoints, their functionalities, and expected input/output formats.
Include sample requests and responses where applicable.
FastAPI was used in remote server using Uvicorn (web server).

# License:
GNU General Public License (GPL) v3
Copyright (C) 2024 Sarah Wilsoncook, Marcel Lommerzheim, Pessi Virta, Jaydeep Bhat

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.


![Dogs all lined up](https://images.unsplash.com/photo-1494947665470-20322015e3a8?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTJ8fGRvZ3N8ZW58MHx8MHx8fDI%3D)
