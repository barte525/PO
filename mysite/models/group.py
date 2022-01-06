from django.db import models


class Group(models.Model):
    country = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
