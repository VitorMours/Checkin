from django.test import TestCase 
import importlib 
import inspect

class TestEmailBackend(TestCase):
    def setUp(self) -> None:
        return super().setUp()
    
    def test_if_is_running(self) -> None:
        self.assertTrue(True)
        
    def test_if_backend_exists(self) -> None: 
        backend_module = importlib.import_module("api.backend")
        self.assertTrue(hasattr(backend_module, "EmailBackend"))
            
    def test_if_backend_have_email_backend_class(self) -> None:
        backend_module = importlib.import_module("api.backend")
        class_ = backend_module.EmailBackend
        self.assertTrue(inspect.isclass(class_))
        self.assertEqual(class_.__name__, "EmailBackend")
        
    def test_if_backend_inherits_from_basebackend(self) -> None:
        backend_module = importlib.import_module("api.backend")
        class_ = backend_module.EmailBackend 
        self.assertTrue(issubclass(class_, importlib.import_module("django.contrib.auth.backends").BaseBackend))
        
    def test_if_authentication_method_exists(self) -> None:
        backend_module = importlib.import_module("api.backend")
        class_ = backend_module.EmailBackend
        self.assertTrue(hasattr(class_, "authenticate"))
        self.assertTrue(callable(getattr(class_, "authenticate")))
        
    def test_if_authentication_method_has_correct_signature(self) -> None:
        backend_module = importlib.import_module("api.backend")
        class_ = backend_module.EmailBackend 
        method = getattr(class_, "authenticate")
        signature = inspect.signature(method)
        parameters = list(signature.parameters.keys())
        self.assertTrue("email" in parameters)
        self.assertFalse("username" in parameters)