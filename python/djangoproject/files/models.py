from django.db import models

import os
from uuid import uuid4

def file_upload_path(instance, filename):
    _, ext = os.path.splitext(filename)
    new_filename = f'{uuid4().hex}{ext}'
    instance.original_filename = filename   # save the original filename in the model
    instance.filename = new_filename   # save the new filename in the model
    return os.path.join('myfiles', str(instance.id), new_filename)

class UploadedFile(models.Model):
    myfile = models.FileField(upload_to=file_upload_path)
    filename = models.CharField(max_length=255, blank=True, null=True)
    original_filename = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.original_filename