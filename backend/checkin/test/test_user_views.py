
from django.test import TestCase
from rest_framework import status

class TestUserViews(TestCase):

    def setUp(self):
        self.users_endpoint_url = "http://localhost:8000/api/users/"
        self.user_data = {
            "first_name": "Test",
            "last_name": "User",
            "email": "testuser@example.com",
            "password": "strong-password-123"
        }

    def test_get_user_view(self):
        """
        Test the GET request to the user list endpoint.
        """
        response = self.client.get(self.users_endpoint_url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_user_view(self):
        """
        Test the POST request to create a new user.
        """
        response = self.client.post(self.users_endpoint_url, data=self.user_data, content_type='application/json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('email', response.json())
        self.assertEqual(response.json()['email'], self.user_data['email'])
        