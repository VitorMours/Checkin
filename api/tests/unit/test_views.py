from django.test import TestCase 
from api.serializers import UserListSerializer
from rest_framework import views
import importlib
import inspect

class TestUserListView(TestCase):
    def setUp(self) -> None:
        pass 
    
    def test_if_is_running(self) -> None:
        self.assertTrue(True)
        
    def test_if_can_import_user_list_view(self) -> None:
        module = importlib.import_module("api.views")
        self.assertTrue(hasattr(module, "UserListView"))
        
    def test_if_view_have_correct_parent_class(self) -> None:
        module = importlib.import_module("api.views")
        class_ = module.UserListView
        self.assertTrue(issubclass(class_, views.APIView))
        
    def test_if_view_have_serializer_class(self) -> None:
        module = importlib.import_module("api.views")
        class_ = module.UserListView
        self.assertTrue(hasattr(class_, "serializer_class"))
        
    def test_if_view_serializer_class_is_correct(self) -> None:
        module = importlib.import_module("api.views")
        serializer_class_ = module.UserListView.serializer_class
        self.assertEqual(serializer_class_, UserListSerializer)
    
    def test_if_view_have_correct_methods(self) -> None:
        methods_list = ["get", "post"]
        module = importlib.import_module("api.views")
        class_ = module.UserListView
        for method in methods_list:
            self.assertTrue(hasattr(class_, method))
    
    def test_post_view_method_signature_have_request_parameter(self) -> None:
        module = importlib.import_module("api.views")
        class_ = module.UserListView
        signature = inspect.signature(class_.post)
        param_names = list(signature.parameters.keys())
        self.assertIn("request", param_names)
        self.assertEqual(param_names[1], "request")