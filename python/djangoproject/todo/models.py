from django.db import models
from django.utils.timezone import now

# Create your models here.

class Todo(models.Model):
    name = models.CharField(max_length=350)
    done = models.BooleanField()
    tiemstamp = models.DateTimeField(default=now())
