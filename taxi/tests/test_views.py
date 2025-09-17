from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from taxi.models import Manufacturer, Car


class SearchTests(TestCase):
    def setUp(self):
        self.manufacturer1 = Manufacturer.objects.create(
            name="Test Manufacturer", country="USA"
        )
        self.car = Car.objects.create(model="Test Car",
                                      manufacturer=self.manufacturer1)
        self.user = get_user_model().objects.create_user(
            username="Test User", email="test@mail.com", password="test1234!"
        )
        self.client.force_login(self.user)

    def test_manufacturer_name_search(self):
        url = reverse("taxi:manufacturer-list")
        response = self.client.get(url, {"query": "Test Manufacturer"})
        self.assertContains(response, "Test Manufacturer")

    def test_car_model_search(self):
        url = reverse("taxi:car-list")
        response = self.client.get(url, {"query": "Test Car"})
        self.assertContains(response, "Test Car")

    def test_driver_username_search(self):
        url = reverse("taxi:driver-list")
        response = self.client.get(url, {"query": "Test User"})
        self.assertContains(response, "Test User")
