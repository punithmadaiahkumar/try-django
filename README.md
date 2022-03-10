# Django 3.2
The fundamentals behind one of the most popular web frameworks in the world by building a real project.
It is a web-framework written in Python and runs the backend for many of the internet's most popular websites such as Instagram and Pinterest.

## Try-Django
Django has so many features that just work out of the box: user authentication, database management, html template rending, URL routing, form data validation, and so much more.


###  Pre-requirements:
+ install Django: `pip install Django `
+ Visual Studio Code [Download](https://code.visualstudio.com/download)
+ install Django with specified version: `pip install "Django>=3.2,<3.3" | pip install Django==3.2.5`
+ upgrade pip: `python -m pip install --upgrade pip`
+ install requirements.txt file: `pip install -r requirements.txt`

### Django command:
+ management command: `python -m django | django-admin`
+ start project: `python -m django startproject <proj_name> .`
+ runserver: `python manage.py runserver`
+ start app: `python manage.py startapp <app_name>`
+ migrations: `python manage.py makemigrations`
+ migrate: `python manage.py migrate`
+ create superuser: `python manage.py createsuperuser`
+ generate secret key: `python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'`

### To execute the project:
+ Run `python manage.py runserver`

### Tutorials:
+ CodingEntrepreneurs [YouTube](https://www.youtube.com/playlist?list=PLEsfXFp6DpzRMby_cSoWTFw8zaMdTEXgL)

+ Refrence to Deployment [App Platform](https://www.codingforentrepreneurs.com/blog/prepare-django-for-digital-ocean-app-platform)

+ To know more about Version Control[GIT Version Control](https://www.codingforentrepreneurs.com/blog/version-control-with-git-basics-for-try-django-32)
