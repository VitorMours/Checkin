from django.db import models
import uuid
# Create your models here.

class Individual(models.Model):
    id = models.UUIDField(default= uuid.uuid4, primary_key=True)
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(null=False, blank=False, unique=True)
    password = models.CharField(max_length=32, null=False, blank=False)

class Admin(Individual):
    pass

class User(Individual):
    pass
