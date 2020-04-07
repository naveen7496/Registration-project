from django.contrib.auth.models import User
from django.db import models


class ExtraInfo(models.Model):
    age = models.IntegerField()
    location = models.CharField(max_length=200)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
