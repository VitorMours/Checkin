from django.test import TestCase 
import importlib
import inspect

class TestUserListView(TestCase):
    def setUp(self) -> None:
        pass 
    
    def test_if_is_running(self) -> None:
        self.assertTrue(True)
        
    def test_if_can_import_user_list_view(self) -> None: