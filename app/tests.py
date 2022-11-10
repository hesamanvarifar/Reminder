from django.test import TestCase
from django.contrib.auth.models import User

from rest_framework.test import APIRequestFactory, force_authenticate
from rest_framework.test import APITestCase

from .views import ReminderList


class ReminderApiTest(APITestCase):
    def setUp(self) -> None:
        self.factory = APIRequestFactory()
        self.user = User.objects.create(username="A")
        self.user.set_password("1234")
        self.user.save()

    def test_authentication(self):

        request = self.factory.get("/api/list/")
        view = ReminderList.as_view()

        response = view(request)
        # check authentication required
        self.assertEqual(response.status_code, 403)

        force_authenticate(request, user=self.user)
        response = view(request)
        self.assertEqual(response.status_code, 200)
