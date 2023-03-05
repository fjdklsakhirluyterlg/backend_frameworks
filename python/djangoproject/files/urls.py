from django.urls import path
from . import views
from pathlib import Path

BASE_DIR = Path.cwd() if "files" not in Path.cwd() else Path.parent()
MEDIA_ROOT =  os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

urlpatterns = [
    path('', views.index, name='index'),
    path('file', views.file, name="file"),
    path('success', views.success, name="success"),
]

from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
