# Social Media API

## Setup
pip install django djangorestframework djangorestframework-authtoken pillow
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

## Endpoints
POST /api/accounts/register/
POST /api/accounts/login/
GET /api/accounts/profile/
