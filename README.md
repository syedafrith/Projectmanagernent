# Projectmanagernent
Project management related restful api's

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/syedafrith/Projectmanagernent.git
$ cd TechForingAssessment
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv2 --no-site-packages venv
$ source venv/bin/activate
```

Then install the dependencies:

```sh
(venv)$ pip install -r requirements.txt
```

Then run makemigrations and migrate

```sh
(venv)$ python manage.py makemigrations
(venv)$ python manage.py migrate
```

Create new superuser with your username and password

```sh
(venv)$ python manage.py createsuperuser
```

Download and import the postman collection from https://github.com/syedafrith/Projectmanagernent/blob/main/TechForingAssessment.postman_collection.json

Run the Django server

```sh
(venv)$ python manage.py runserver
```





