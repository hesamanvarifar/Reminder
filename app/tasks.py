from datetime import datetime, timedelta

from celery import shared_task

from .models import Reminder


@shared_task
def reminder_reports():
    qs = Reminder.objects.filter(remind_date=datetime.date())
    for reminde in qs:
        print("its time to check your reminder")

    queryset = Reminder.objects.all()
    for remind in queryset:
        if remind.remind_date - datetime.date() == timedelta(days=3):
            print("be careful! your reminder, reminde you 3 days later!")
