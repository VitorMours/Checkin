from django.test import TestCase 
from django.urls import path as django_path
import importlib
import inspect

class TestUrls(TestCase):
    def setUp(self) -> None:
        self.module = importlib.import_module("api.urls")
        self.urls = [
            'auth/login',
            'auth/token/refresh/',
            'auth/token/verify/',
        ]        
    
    def test_if_is_running(self) -> None:
        self.assertTrue(True)
    
    def test_if_contains_urlpatterns(self) -> None:
        self.assertTrue(hasattr(self.module, "urlpatterns"))
        self.assertTrue(isinstance(getattr(self.module, "urlpatterns"), list))
                
    def test_if_urlpatterns_contains_expected_urls(self) -> None:
        urlpatterns = getattr(self.module, "urlpatterns")
        for path in urlpatterns:
            if path.pattern._route in self.urls:
                self.urls.remove(path.pattern._route)
                
        self.assertEqual(len(self.urls), 0, f"Existe uma rota faltando: {self.urls}")                
        
        
    