## Deploy Python App to Azure from VSC
Create a **production.py** with following code 
```
//production.py

from .settings import *
import os

# When azure deploys the app, it sets the WEBSITE_HOSTNAME environment variable automatically.
ALLOWED_HOSTS = [os.environ['WEBSITE_HOSTNAME']] if 'WEBSITE_HOSTNAME' in os.environ else []

DEBUG = True  // set to True only as long as you want to debug the production


```

this will extend the settings.py, when the app is published to production.

In manage.py set the follwing
```
//manage.py

def main():
    settings_module = '<projectappName>.production' if 'WEBSITE_HOSTNAME' in os.environ else '<projectappName>.settings'
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)

    ... rest of code
```

And set this in wsgi.py
```
//wsgi.py

import os
from django.core.wsgi import get_wsgi_application

settings_module = '<projectappName>.production' if 'WEBSITE_HOSTNAME' in os.environ else '<projectappName>.settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)
application = get_wsgi_application()

```
# Please check!!
## important
for some reason, I had to take out **SECRET_KEY = 'django-insecure-lji85=9nb@kemrp9-n^(0gea#6h4l%!h8epmbegek1zp7j(mpi'** out of the **.env** file and call the django secret directly in settings.py