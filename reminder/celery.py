import os
from celery import Celery
from celery.schedules import crontab
from decouple import config

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "reminder.settings")

app = Celery("reminder")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
app.conf.beat_schedule = {
    "add-every-morning": {
        "task": "tasks.add",
        "schedule": crontab(hour=7, minute=30, day_of_week=7),
        "args": (16, 16),
    },
}
