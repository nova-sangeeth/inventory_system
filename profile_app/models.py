from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class user_profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=256, null=True)
    age = models.PositiveIntegerField(null=True)
    address = models.CharField(max_length=256, null=True)
    phone = models.CharField(max_length=15, null=True)
    pincode = models.CharField(max_length=7, null=True)

    def __str__(self):
        return self.name
