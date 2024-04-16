from unicodedata import name
from django.db import models

# Create your models here.

class Contact (models.Model):
    name = models.CharField(max_length=256, blank=False)
    phone = models.IntegerField(blank=False)
    address = models.TextField(max_length=256, blank=False)
    created_ts = models.DateTimeField(auto_now_add=True)
    updated_ts = models.DateTimeField(auto_now=True)