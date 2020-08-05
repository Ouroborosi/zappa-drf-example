# Servless Python with Zappa
## Introduction
The Zappa is a tool which claim "no permeanent infrastructure". It helps to build and deploy the servless Python app on AWS Lambda + API Gateway.

This example project is going to build a simple TODO app with Zappa, Django and DRF.

## Requirements
Create an virtual environment for the project.
```shellscript
# (optional) install the virtualenv if you haven't install yet
pip install virtualenv

virtualenv env
```

The project requires the following:
```shellscript
pip install django djangorestframework zappa
```

## Creation
### Create project.
```shellscript
django-admin startproject servless_python_with_zappa
```

(Optional) Rename the servless_python_with_zappa project to `src`.

### Create App
Change directory under the project folder and create app.
```shellscript
cd src/
python manage.py startapp core
```

Add `rest_framework` in the `settings.py`.
```python
INSTALLED_APPS = [
    ...
    'rest_framework',
]
```
