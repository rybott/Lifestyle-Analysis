from django.db import models


class Transactions(models.Model):
    fname = models.CharField(max_length=50, null=True, blank=True)  # First Name
    lname = models.CharField(max_length=50, null=True, blank=True)  # Last Name
    phone = models.CharField(max_length=11, null=True, blank=True) 