from django.test import TestCase
from api.models import User, Admin



class AnimalTestCase(TestCase):
    def setUp(self) -> None:
        self.user_carlos = User.objects.create(first_name = "Carlos", 
                                               last_name="Vitor", 
                                               email="carlos.vitor@email.com", 
                                               password="123123sad"
                                               )     

    def test_get_object_first_name(self) -> None:
        self.assertEqual(self.user_carlos.first_name, "Carlos")   