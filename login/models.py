from django.db import models


class Users(models.Model):
    loginw = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
