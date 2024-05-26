## Setup
- Create the virtual environment with `python -m venv env`. See yes, when VSC alerts you to set Workspace folder
- then activate virtual env `.\env\Scripts\activate`
*You now see **(env)** in front of your command line*
- Next, install all dependencies with `pip install -r requirements.txt`
*All dependencies are going to be installed into the venv*
- Check your db by running `python manage.py makemigrations` and then create the data base with `python manage.py migrate`
- Now, create an administrator for your db with `python manage.py createsuperuser`. Give a name, email and password when prompted.
- Now run the server with `python manage.py runserver`

## Azure Settings
Set the correct paths in settings.py

```
//settings.py

ALLOWED_HOSTS = ['localhost:4200','127.0.0.1',]

CORS_ALLOWED_ORIGINS = ['http://localhost:4200','https://kanban.azurewebsites.net']
CSRF_TRUSTED_ORIGINS = ['https://kanban-backend.azurewebsites.net']

.... weiter unten für die static files

ROOT_URLCONF = 'konferenzbackend.urls'
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

## Authentication
To decide, how storage settings are authenticated see: [README](README.md)