from django.test import TestCase, Client

from api.utils import validate_json_header

class UsersEndpointTestCase(TestCase):

    def setUp(self) -> None:
        self.client = Client(headers={"Content-Type": "application/json"})
        self.client_html_header = Client(headers={"Content-Type": "text/html"})

    def test_get_users_list_endpoint(self) -> None:
        response = self.client.get("/api/users/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.charset, "utf-8")
        self.assertIn("Content-Type", response.headers)
        self.assertEqual(response.headers["Content-Type"], "application/json")

    def test_get_users_list_with_wrong_header(self) -> None: 
        response = self.client_html_header.get("/api/users/")
        self.assertEqual(response.status_code, 400)

    def test_post_users_list_endpoint(self) -> None:
        response = self.client.post("/api/users/", data={}) # TODO: Adicionar os dados do usuario


