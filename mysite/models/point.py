from django.db import models


class Point(models.Model):
    name = models.CharField(max_length=200)
