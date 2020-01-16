# We Use an official Python runtime as a parent image
FROM python:3.5
# create root directory for our project in the container
RUN mkdir /docker_mopga
# Set the working directory to /mopga
WORKDIR /mopga
# Copy the current directory contents into the container at /mopga
ADD . /mopga/
# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt
