from django.db import models
from django.contrib.auth.models import User, Group

class Administrator(User):
    pass

class Administrated(User):
    pass


class Sector(models.Model):
    name = models.CharField(max_length=50)


