from django.db import models
from .group import Group


class Range(models.Model):
    country = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    group = models.ForeignKey(Group, on_delete=models.PROTECT)
