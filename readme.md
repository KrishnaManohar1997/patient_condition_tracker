# Project Setup

### Creating Virtual Environment
`python -m venv .env`

Once the environment is activated
Install all the requirements of the project using the following command

`pip install -r requirements.txt`

Currently we are using the default sqlite db that comes with Django

# Steps to recreate project creation

## Creating the django project
`django-admin startproject patient_condition_tracker`

## Adding apps to the project

`python manage.py startapp patient`

### Add this newly created app into the list of INSTALLED_APPS list under settings.py`

## Executing initial migrations
`python manage.py migrate`

## Attaching pre-commit
Execute the following command in the virtual env activated shell
`pre-commit install`
## Implemented Features
- Patient and Disease Model
- CRUD operations on the Patient and Disease Views
- Pagination for the list-apis
- Structured the App in MVC-like format

Code standards
- Used Black formatter to format the code and flake8 linter
- snake_case as standard for methods and variable names
- PascalCase for classes and Database names
- Added pre-commit hooks for the project to maintain code standards

## Things that can be implemented
- Authentication system [Token or JWT]
- Media Upload mechanism for Uploading/Changing avatar