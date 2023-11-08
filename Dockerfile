# Use an official Python runtime as a parent image
FROM python:3.8

# Set environment variables for Python (you can adjust these as needed)
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE myproject.settings

# Create and set the working directory inside the container
RUN mkdir /app
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Copy the rest of the application code into the container at /app
COPY . /app/
