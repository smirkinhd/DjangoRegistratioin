from django.db import models
from django.contrib.auth.models import User 

class CustomUser (User ):
    middle_name = models.CharField(max_length=30, blank=True)
    phone_number = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return self.username
