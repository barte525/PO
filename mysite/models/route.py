from django.db import models
from .user import Tourist


class Route(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    tourist = models.ForeignKey(Tourist, on_delete=models.CASCADE)
