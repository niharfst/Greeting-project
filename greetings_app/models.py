# greetings_app/models.py
from django.db import models

class UserGreeting(models.Model):
    name = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

