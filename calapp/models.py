from time import time
from django.db import models
from django.utils import timezone
import datetime
from datetime import datetime as ti


# Create your models here.
class add_spends(models.Model):
    spend_CHOICES = (
    ("spend", "spend"),
    ("get", "get"),
)
    reason=models.CharField(max_length=100)
    amount=models.IntegerField(max_length=100)
    type=models.CharField(max_length=100,choices=spend_CHOICES)
    date=models.DateTimeField(auto_now_add=True)
