## Django Tutorial - Polls Web Application

This repository was created to begin the learning of django web framework

## Version support

Django

	Version 1.9.6
Python

	Python 3.5.1

## Quick Start

	$ git clone git@github.com:sohjunjie/django-tutorial.git

- Install Postgres
- Install Python
- Install Pip
- Install Django and required packages using

		pip install -r requirements.txt

- Create a database for the project on Postgres. Ensure you are in postgres console

		# CREATE USER mydb;

- Create tables in database by running

        $ python manage.py migrate

- Load seed data to database by running

        $ python manage.py loaddata seed_data.json

- You can also create seed data with current database table by running

      	$ python manage.py dumpdata --natural-foreign --natural-primary --indent=2 -e sessions -e admin -e contenttypes -o seed_data.json

After seeding, the default login for the django admin is:

user: postgres
pass: qwe123qwe123
