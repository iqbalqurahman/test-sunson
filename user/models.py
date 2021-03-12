#User/models.py
from django.db import models

class User(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    telp = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    deleted = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
