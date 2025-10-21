from __future__ import annotations
from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.db import models
class CustomUserManager(UserManager):
    def create_user(self, email, password, first_name, **extra_fields) -> CustomUser:
        if not email or not password or not first_name:
                raise ValueError(_("A required value was not passed"))

        email = self.normalize_email(email)

        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_staff", False)
        
        user = self.model(
            first_name=first_name,
            email=email,
            **extra_fields)        
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, first_name, **extra_fields) -> None:
        if not email and not password and not first_name:
            return ValueError(_("A required value was not passed"))
        
        email = self.normalize_email(email)
        user = self.model(
            email = email,
            first_name = first_name,
            is_staff=True 
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

class CustomUser(AbstractBaseUser, PermissionsMixin):

    first_name = models.CharField(max_length=50, blank=False, null=False)
    last_name = models.CharField(max_length=50, null=False, blank=True)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ("first_name","password",)
        
    objects = CustomUserManager()


