from django.db import models
from django.utils.timezone import now

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=350)
    done = models.BooleanField(default=False)
    tiemstamp = models.DateTimeField(default=now())
