from django.db import models
from django.utils import timezone
# Create your models here.

class Message(models.Model):
    ts = models.DateTimeField(default=timezone.now)
    msg = models.TextField()
    hashkey = models.CharField(max_length=6)
