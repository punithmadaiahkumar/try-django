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

### Django commands:
+ management command: `python -m django | django-admin`
+ start project: `python -m django startproject <proj_name> .`
+ runserver: `python manage.py runserver`
+ start app: `python manage.py startapp <app_name>`
+ migrations: `python manage.py makemigrations`
+ migrate: `python manage.py migrate`
+ create superuser: `python manage.py createsuperuser`
+ generate secret key: `python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'`
+ shell:    `python manage.py shell`
+ data dump:    `python manage.py dumpdata <filename> --indent 4`
+ data dump to folder:  `python manage.py dumpdata recipes --indent 4 > <directory name>/<filename>.json`

### Github Configure:
Configure you Github in you command prompt/terminal for initilizing you git process.
+ configure name:   `git config user.name "<your name>"`
+ configure email:  `git config user.email "<you email>"`

### Git and Github Commands:
+ git repo creating:   `crete a public/private repo in github `
+ delete ur .git file/folder from ur local directory:		`rm -ef .git (mac)` | `rmdir .git (windows)` 
+ to start initilize:	`git init`
+ to add origin/host: 	`git remote add origin <url of github repo>.git`
+ to check status:		`git status (to track ur file upload in git repo)`
+ to add particular file:   `git add <filename>/ `
+ to add all file:   `git add --all (mac)` | `git add -A (windows)`
+ commit ur changes:		`git commit "<type you commit message>"`
+ reset commit:		`git reset <commit id> --hard`
+ check your remote host:	`git remote (this will tell where ur repo is)`
+ describe your remote host:     `git remote -v (this give a robost description on host)`
+ delete/remove host:		`git remote remove <name>` 
+ push you commit:		`git push <ur branch>` (if u have a specified branch add that or, use main or master to push)
+ to check log:		`git log`



### To execute the project:
+ Run `python manage.py runserver`

### Reference\Tutorials:
+ Local refrence for QuerySets and Lookups, Generating Secret Key, Writing & Reading Data via models [Refrences](/refrences).

+ CodingEntrepreneurs [YouTube](https://www.youtube.com/playlist?list=PLEsfXFp6DpzRMby_cSoWTFw8zaMdTEXgL).

+ Refrence to Deployment [App Platform](https://www.codingforentrepreneurs.com/blog/prepare-django-for-digital-ocean-app-platform).

+ To know more about Version Control [GIT Version Control](https://www.codingforentrepreneurs.com/blog/version-control-with-git-basics-for-try-django-32).

+ Django pre_save and post_save [Django doc](https://docs.djangoproject.com/en/4.0/ref/signals/).


