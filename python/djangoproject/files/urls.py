from django.urls import path
from . import views
from pathlib import path

BASE_DIR = 
MEDIA_ROOT =  os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

urlpatterns = [
    path('', views.index, name='index'),
    path('file', views.file, name="file"),
    path('success', views.success, name="success"),
]