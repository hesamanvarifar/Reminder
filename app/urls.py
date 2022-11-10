from django.urls import path
from .views import ReminderList, ReminderDetail, ReminderDelete, ReminderUpdate

urlpatterns = [
    path("list/", ReminderList.as_view()),
    path("detail/", ReminderDetail.as_view()),
    path("delete/", ReminderDelete.as_view()),
    path("update/", ReminderUpdate.as_view()),
]
