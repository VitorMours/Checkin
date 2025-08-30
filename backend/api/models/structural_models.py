from django.db import models
from django.db.models import Manager
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, UserManager
import uuid
from datetime import date
from django.utils import timezone


class Sector(models.Model):
    id =models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    name = models.CharField(max_length=75, null=False, blank=False)
    code = models.CharField(max_length=8, unique=True, null=True, blank=False)
    created_at = models.DateTimeField(default=timezone.now(), editable=False)

class Journey(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    start_time = models.TimeField(null=False, blank=False)
    end_time = models.TimeField(null=False, blank=False)
    start_date = models.DateField(default=date.today)
    end_date = models.DateField(null=False, blank=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def set_same_day(self) -> None:
        if self.start_date is None:
            return ValueError("Start day must have a value to be the same as the end date")
        
        self.end_date = self.start_date
        