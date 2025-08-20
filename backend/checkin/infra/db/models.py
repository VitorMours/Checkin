import uuid
from django.db import models
from django.contrib.auth.models import User, AbstractUser, Group

# class Administrator(User):
    # pass

# class Administrated(User):
    # pass

class User(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    first_name = models.CharField(max_length=255, null=False, blank=False, default="Inexistente")
    last_name = models.CharField(max_length=255, null=False, blank=False, default="da Silva")
    email = models.EmailField(unique=True, null=False, blank=False)
    password = models.CharField(max_length=128, null=False, blank=False)  # armazene hash, use set_password()

    class Meta:
        db_table = "users"
        app_label = "infra"

    def set_password(self, raw_password):
        from django.contrib.auth.hashers import make_password
        self.password = make_password(raw_password)

class Sector(models.Model):
    name = models.CharField(max_length=50)
    boss = models.CharField(max_length=113)

    due_date = models.DateField(null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)


    class Meta:
        app_label = "infra" 
        db_table="sectors"