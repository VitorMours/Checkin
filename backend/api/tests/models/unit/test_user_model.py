import json
from django.test import TestCase
from api.models import User


class UserModelTestCase(TestCase):
    def setUp(self) -> None:
        self.user_carlos = User.objects.create(first_name = "Carlos", 
                                               last_name="Vitor", 
                                               email="carlos.vitor@email.com", 
                                               password="123123sad"
                                               )     

    def test_get_object_first_name_data(self) -> None:
        self.assertEqual(self.user_carlos.first_name, "Carlos")     
    
    def test_get_object_last_name_data(self) -> None:
        self.assertEqual(self.user_carlos.last_name, "Vitor")
        
    def test_get_object_email_data(self) -> None:
        self.assertEqual(self.user_carlos.email, "carlos.vitor@email.com")

    def test_set_object_first_name_data(self) -> None:
        self.assertEqual(self.user_carlos.first_name, "Carlos")
        self.user_carlos.first_name = "Lucas"
        self.assertEqual(self.user_carlos.first_name, "Lucas")


    def test_set_object_last_name_data(self) -> None:
        self.assertEqual(self.user_carlos.last_name, "Vitor")
        self.user_carlos.last_name = "Pietro"
        self.assertEqual(self.user_carlos.last_name, "Pietro")

    def test_set_object_email_data(self) -> None:
        self.assertEqual(self.user_carlos.email, "carlos.vitor@email.com")
        self.user_carlos.email = "teste.teste@email.com"
        self.assertEqual(self.user_carlos.email, "teste.teste@email.com")

    def test_set_object_first_name_null_or_blank(self) -> None:
        self.assertEqual(self.user_carlos.first_name, "Carlos")



