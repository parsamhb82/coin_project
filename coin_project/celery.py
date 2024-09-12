import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "coin_project.settings")

app = Celery('coinproject')
