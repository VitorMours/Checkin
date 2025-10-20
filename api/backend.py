from django.contrib.auth.backends import BaseBackend

class EmailBackend(BaseBackend):
    """
    Custom authentication that uses the email field to authenticate users 
    inside of the database and the system.
    """
    def authenticate(self, request, email=None, password=None, **kwargs):
        pass