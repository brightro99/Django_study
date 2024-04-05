# Django & Flutter

https://youtube.com/playlist?list=PLsGh7Wc318kjAd93kqSw9O4xGuu4BZAHZ&si=X9DO2pJckUWQioDx

## Install
```
conda create --name django python=3.9
conda activate django
pip install Django
pip install djangorestframework
pip install markdown       # Markdown support for the browsable API.
pip install django-filter  # Filtering support
```

## Start
```
django-admin startproject django_api
python3 manage.py startapp plan
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py createsuperuser
python3 manage.py runserver
```