from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from restaurant.models import Menu

class MenuViewTest(TestCase):
    def setUp(self):
        # Create some Menu instances for testing
        self.menu1 = Menu.objects.create(ID=101,Title="Burger", Price=5.99, Inventory=20)
        self.menu2 = Menu.objects.create(ID=100,Title="Pizza", Price=8.99, Inventory=20)
        self.client = APIClient()

    def test_get_all(self):
        # Make a GET request to retrieve all Menu objects
        response = self.client.get('/restaurant/menu/')  # Update this URL to your Menu API endpoint

        # Check if the response status is OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Ensure the response contains serialized data of the two menu items
        self.assertEqual(len(response.data), 2)

        # Check if the serialized data matches expected values (could depend on your serializer)
        self.assertEqual(response.data[0]['Title'], 'Pizza')
        self.assertEqual(response.data[1]['Price'], '5.99')


