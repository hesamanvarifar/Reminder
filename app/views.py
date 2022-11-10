from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
)
from rest_framework import authentication, permissions

from .models import Reminder
from .serializer import ReminderSerializer


class ReminderList(ListCreateAPIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    queryset = Reminder.objects.all()
    serializer_class = ReminderSerializer


class ReminderDetail(RetrieveAPIView):

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    queryset = Reminder.objects.all()
    serializer_class = ReminderSerializer


class ReminderUpdate(UpdateAPIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    queryset = Reminder.objects.all()
    serializer_class = ReminderSerializer


class ReminderDelete(DestroyAPIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    queryset = Reminder.objects.all()
    serializer_class = ReminderSerializer
