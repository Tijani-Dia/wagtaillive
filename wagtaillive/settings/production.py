from .base import *
import os
import dj_database_url

DEBUG = False

SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = ["mighty-thicket-51832.herokuapp.com"]

DATABASES = {}
DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)

BASE_URL = 'http://example.com'

SLACK_SIGNING_SECRET = os.environ['SLACK_SIGNING_SECRET']
SLACK_BOT_TOKEN = os.environ['SLACK_BOT_TOKEN']

PIESOCKET_API_KEY = os.environ['PIESOCKET_API_KEY']
PIESOCKET_SECRET = os.environ['PIESOCKET_SECRET']
PIESOCKET_ENDPOINT = "free3.piesocket.com/v3/"
