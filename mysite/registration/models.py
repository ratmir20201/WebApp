from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(null=False, blank=False, max_length=100)
    phone_number = models.CharField(null=True, blank=True, max_length=11)
