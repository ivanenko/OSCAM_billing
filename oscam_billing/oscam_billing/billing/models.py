from django.db import models
from django.contrib.auth.models import User

class Package(models.Model):

    name = models.CharField(blank=True, max_length=10, null=True)
    field2 = models.CharField(blank=True, max_length=10, null=True)
    field3 = models.CharField(blank=True, max_length=10, null=True)
    field4 = models.CharField(blank=True, max_length=10, null=True)


class Payment(models.Model):
    user = models.ForeignKey(User)
    date = models.DateTimeField()
    method = models.IntegerField()
    summ = models.DecimalField(max_digits=10, decimal_places=2)