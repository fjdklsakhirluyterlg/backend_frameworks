from django.db import models

# Create your models here.

class Todo(models.Model):
    models.CharField(max_length=350)
    