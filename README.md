# Django Band Website

## Table of Contents

- [Project Description](#project-description)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Docker](#docker)
- [Project Author](#project-author)

## Project Description

Django Band Website is a web project that allows you to create a website for a fictional band using the Django framework. Whether you're managing a real band or just want to experiment with web development, this project provides a solid foundation for building a band website.

## Project Structure

The project is organized into the following directories:

- `capstone/`: Contains Django project settings and configurations.
- `band/`: The Django app for the band website.
- `media/`: Stores files uploaded to database
- `static/`: Houses static files such as CSS, JavaScript, and images.

## Installation

To run this project on your local system, follow these steps:

1. Clone the repository from GitHub:

   ```bash
   git clone https://github.com/nokuthabam/django-band-website.git

2. Install project dependencies:
   - pip install -r requirements.txt
     
2. Installing Django and creating virtual environment:
   - mkvirtualenv my_django
   - workon my_django
   -  pip install django
  
3. Navigate to the project directory:
   - cd django-band-website/capstone

3. Apply database migrations:
   - python manage.py migrate

4. Create a superuser to manage the Django admin panel:
   - python manage.py createsuperuser

5. Start the development server:
   - python manage.py runserver

6. Access the website at http://127.0.0.1:8000/

## Usage
   - Visit http://127.0.0.1:8000/ to access the landing page
   - Click "Explore" to go to the login page, where you can sign up or log in if you have credentials.
   - Once logged in, you can navigate through the website's various pages.

## Docker
   - In order to run using the docker image, use the following commands
   1. To download the image from docker hub:
      - docker pull nmoyo45/django_website:latest

   2. To run the image
      - docker run -it -p 8000:8000 nmoyo45/django_website:latest python manage.py runserver 0.0.0.0:8000
   3. To access the Landing Page:
      - Visit http://127.0.0.1:8000/ or http://localhost:8000/
      - Click "Explore" to go to the login page, where you can sign up or log in if you have credentials.
      - Once logged in, you can navigate through the website's various pages.

## Project Author
Nokuthaba Moyo

Feel free to explore and customize the Django Band Website to suit your band or project needs.