from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.db import models
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields) -> None:
        pass 
    
    def create_superuser(self) -> None:
        pass




class CustomUser(AbstractBaseUser, PermissionsMixin):
    USERNAME_FIELD = "email"

    first_name = models.CharField(max_length=50, blank=False, null=False)
    email = models.EmailField(unique=True)
    
    objects = CustomUserManager()
