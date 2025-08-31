import json
from django.test import TestCase
from api.models import User


class SectorModelTestCase(TestCase):
      def setUp(self) -> None:
        self.user_carlos = User.objects.create(first_name = "Carlos", 
                                               last_name="Vitor", 
                                               email="carlos.vitor@email.com", 
                                               password="123123sad",
                                               
                                               )     

      def test_sector_has_id(self) -> None:
            pass 
    

      def test_sector_has_code(self) -> None:
           pass 

      def test_sector_has_name(self) -> None:
           pass

