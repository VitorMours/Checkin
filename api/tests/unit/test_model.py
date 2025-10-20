from django.test import TestCase 
import importlib 
import inspect

class TestCustomUserModel(TestCase):
    def setUp(self) -> None:
        self.module = importlib.import_module("api.models")
        
    def test_if_is_running(self) -> None:
        self.assertTrue(True)

    def test_if_custom_user_model_exists(self) -> None:
        self.assertTrue(hasattr(self.module, "CustomUser"))
        
    def test_if_custom_user_is_a_class(self) -> None:
        class_ = self.module.CustomUser 
        self.assertTrue(inspect.isclass(class_))
        
    def test_if_custom_user_inherits_from_abstract_model(self) -> None:
        class_ = self.module.CustomUser 
        self.assertTrue(issubclass(class_, importlib.import_module("django.contrib.auth.models").AbstractBaseUser))
        self.assertTrue(issubclass(class_, importlib.import_module("django.contrib.auth.models").PermissionsMixin))
    
    def test_if_custom_user_model_have_username_field(self) -> None:
        class_ = self.module.CustomUser 
        self.assertTrue(hasattr(class_, "USERNAME_FIELD"))
        self.assertTrue(getattr(class_, "USERNAME_FIELD"), "email")

class TestCustomUserManager(TestCase):
    def setUp(self) -> None:
        self.necessary_methods = ["create_user", "create_superuser"]
        self.module = importlib.import_module("api.models")
    
    def test_if_custom_user_manager_exists(self) -> None:
        self.assertTrue(hasattr(self.module, "CustomUserManager"))
       
    def tet_if_custom_user_manager_is_a_class(self) -> None: 
        class_ = self.module.CustomUserManager
        self.assertTrue(inspect.isclass(class_))
        
    def test_if_custom_user_manager_inherits_corectly(self) -> None:
        class_ = self.module.CustomUserManager 
        self.assertTrue(issubclass(class_, importlib.import_module("django.contrib.auth.models").BaseUserManager))
        
    def test_if_custom_user_manager_is_assigned_to_custom_user(self) -> None:
        user_class = self.module.CustomUser 
        self.assertTrue(hasattr(user_class, "objects"))
        self.assertTrue(isinstance(getattr(user_class, "objects"), self.module.CustomUserManager))
        
    def test_if_custom_user_manager_have_create_user_method(self) -> None:
        class_ = self.module.CustomUserManager
        self.assertTrue(hasattr(class_, "create_user"))
        
    def test_if_custom_user_manager_have_create_superuser_method(self) -> None:
        class_ = self.module.CustomUserManager
        self.assertTrue(hasattr(class_, "create_superuser"))
        
    def test_if_custom_user_manager_create_user_function_return_user(self) -> None: 
        pass

        
    