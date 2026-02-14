from pathlib import Path
#from dotenv import load_dotenv
from os import getenv, path
from .base import *
from .base import BASE_DIR

local_env = path.join(BASE_DIR, '.env', '.env.local')

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = getenv("DEBUG")

ALLOWED_HOSTS = ["localhost", "127.0.0.1", "0.0.0.0"]

