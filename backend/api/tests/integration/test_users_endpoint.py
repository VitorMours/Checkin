from django.test import TestCase, Client

class UsersEndpointTestCase(TestCase):

    def setUp(self) -> None:
        self.client = Client()
        self.client_html_header = Client(headers={"Content-Type": "text/html"})

    def test_get_users_list_endpoint(self) -> None:
        response = self.client.get("/api/users/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.charset, "utf-8")
        self.assertIn("Content-Type", response.headers)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        
        assert True

    def test_get_users_list_with_wrong_header(self) -> None: 
        response = self.client_html_header.get("/api/users/")

    def test_post_users_list_endpoint(self) -> None:
        pass


