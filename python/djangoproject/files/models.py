from django.db import models

# Create your models here.

class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/%Y/%m/%d/')
    uploaded_at = models.DateTimeField(auto_now_add=True)