from .settings import *
import os

# When azure deploys the app, it sets the WEBSITE_HOSTNAME environment variable automatically.
ALLOWED_HOSTS = [os.environ['WEBSITE_HOSTNAME']] if 'WEBSITE_HOSTNAME' in os.environ else []

DEBUG = True