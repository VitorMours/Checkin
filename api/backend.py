from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model

class EmailBackend(BaseBackend):
    """
    Custom authentication that uses the email field to authenticate users 
    inside of the database and the system.
    """
    def authenticate(self, request, email=None, password=None, **kwargs):
        user_model = get_user_model()
        try:
            user = user_model.objects.get(email=email)
        except user_model.DoesNotExist: 
            return None 
        
        if user.check_password(password):
            return user
        return None
        
    def get_user(self, user_id) -> None:
        user_model = get_user_model()
        try:    
            user = user_model.objects.get(id=user_id)
            
        except user_model.DoesNotExist:
            return None