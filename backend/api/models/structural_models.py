from django.db import models
from django.db.models import Manager
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, UserManager
import uuid
from datetime import date
from django.utils import timezone
from api.models.models import User

class Sector(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    name = models.CharField(max_length=75, null=False, blank=False)
    code = models.CharField(max_length=8, unique=True, null=True, blank=False)
    created_at = models.DateTimeField(default=timezone.now(), editable=False)

    def __repr__(self) -> str:
        return f"<Sector: {self.name} {self.code} [{self.created_at}]>"

class Journey(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    start_time = models.TimeField(null=False, blank=False)
    end_time = models.TimeField(null=False, blank=False)
    start_date = models.DateField(default=date.today)
    end_date = models.DateField(null=False, blank=False)
    individual = models.OneToOneField(User, on_delete=models.CASCADE)
    sector = models.OneToOneField(Sector, on_delete=models.CASCADE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def set_same_day(self) -> None:
        if self.start_date is None:
            return ValueError("Start day must have a value to be the same as the end date")
        self.end_date = self.start_date
        
    def __repr__(self) -> str:
        return f"<Journey: {self.start_date} -> {self.end_date}; {self.start_time} -> {self.end_time} == {self.individual}>"
