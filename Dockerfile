# Use an official Python runtime as a parent image
FROM python:3.8

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Expose port 8000
EXPOSE 8000

# Collect static files (if applicable to your Django project)
RUN python manage.py collectstatic --noinput

# Make migrations and apply them (if applicable)
RUN python manage.py makemigrations
RUN python manage.py migrate

# Start the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]