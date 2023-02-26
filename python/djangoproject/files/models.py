from django.db import models

import os
from uuid import uuid4

def file_upload_path(instance, filename):
    _, ext = os.path.splitext(filename)
    new_filename = f'{uuid4().hex}{ext}'
    return os.path.join('myfiles', str(instance.id), new_filename)

# Create your models here.

class UploadedFile(models.Model):
    file = models.FileField(upload_to=file_upload_path)
    uploaded_at = models.DateTimeField(auto_now_add=True)