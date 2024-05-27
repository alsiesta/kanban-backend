from pathlib import Path
import os
from dotenv import load_dotenv

from django.core.files.storage import Storage 

# from home.azure_storage import AzureBlobStorage

load_dotenv()


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost:4200','127.0.0.1','orange-beach-0362aa803.5.azurestaticapps.net']

CORS_ALLOWED_ORIGINS = ['http://localhost:4200','https://kanban.azurewebsites.net']
CSRF_TRUSTED_ORIGINS = ['https://kanban-backend.azurewebsites.net','https://orange-beach-0362aa803.5.azurestaticapps.net']

# CORS_ALLOW_ALL_ORIGINS = True

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'posts',
    'home',
    'storages',  # needed for Azure Blob Storage
    'kanban',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    # ...
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'konferenzbackend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

ROOT_URLCONF = 'konferenzbackend.urls'
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ]
}


# ---------------------------- # ---------------------------- #
# #AUTHENTICATION USING ACCOUNT KEY############################
# #AUTHENTICATION USING ACCOUNT KEY############################
# #AUTHENTICATION USING ACCOUNT KEY############################

# COMMENT OUT THE FOLLOWING IF YOU WANT TO USE MANAGED IDENTITY
DEFAULT_FILE_STORAGE = 'storages.backends.azure_storage.AzureStorage'
AZURE_ACCOUNT_NAME = 'dlastor'
AZURE_ACCOUNT_KEY = os.getenv('AZURE_ACCOUNT_KEY')
AZURE_CONTAINER = 'kanban-media'
AZURE_OVERWRITE_FILES = True  # Set to True or False based on your preference
AZURE_URL_EXPIRATION_SECS = None
AZURE_SSL = True
# COMMENT OUT ABOVE IF YOU WANT TO USE MANAGED IDENTITY

# # In case you want to use Azure for static files
# STATICFILES_STORAGE = 'storages.backends.azure_storage.AzureStorage'
# AZURE_STATIC_CONTAINER = 'your_static_container_name'


# ---------------------------- # ---------------------------- #
# #########AUTHENTICATION USING MANAGED IDENTITY###############
# #########AUTHENTICATION USING MANAGED IDENTITY###############
# #########AUTHENTICATION USING MANAGED IDENTITY###############


# # COMMENT OUT THE FOLLOWING IF YOU WANT TO USE ACCOUNT KEY
# DEFAULT_FILE_STORAGE = 'home.azure_storage.AzureBlobStorage' # this complete class is defined in home/azure_storage.py and it handles all the storage operations used by Django Admin and other parts of the application

