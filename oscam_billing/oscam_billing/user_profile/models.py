from billing.models import Package
from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    dealer = models.ForeignKey(User, related_name='dealer')
    comission = models.DecimalField(blank=True, max_digits=5, decimal_places=2, null=True)
    notes = models.CharField(blank=True, max_length=100, null=True)
    open_password = models.CharField(blank=True, max_length=20)

    packages = models.ManyToManyField(Package)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username
