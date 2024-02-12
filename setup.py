# setup.py
from setuptools import setup, find_packages

with open("requirements.txt") as f:
    content = f.readlines()
    requirements = [x.strip() for x in content if "git+" not in x]

setup(name='snoop_dog',
      version="0.0.1",
      description="A model to classify dog breeds",
      packages=find_packages(), # You can have several packages, try it
      install_requires=requirements
)
