from django.test import TestCase 

class TestSettings(TestCase):
    def test_if_is_running(self) -> None: 
        self.assertTrue(True)
        
    def test_if_django_is_installed(self) -> None:
        try: 
            import django 
            self.assertTrue(True)
        except ImportError:
            self.fail("Django is not installed")
        
    def test_if_django_rest_framework_is_installed(self) -> None: 
        try: 
            import rest_framework 
            self.assertTrue(True)
        except ImportError:
            self.fail("Django REST Framework is not installed")
            
    def test_if_simplejwt_is_installed(self) -> None: 
        try: 
            import rest_framework_simplejwt 
            self.assertTrue(True)
        except ImportError:
            self.fail("Django REST Framework SimpleJWT is not installed")
            
    def test_if_corsheaders_is_installed(self) -> None:
        try:
            import corsheaders 
            self.assertTrue(True)
        except ImportError: 
            self.fail("Django cors headers not installed")