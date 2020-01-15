# We Use an official Python runtime as a parent image
FROM python:3.5


RUN mkdir ./test
# Set the working directory to /music_service
WORKDIR ./test
# Copy the current directory contents into the container at /music_service
ADD ../mopga ./test
# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt
