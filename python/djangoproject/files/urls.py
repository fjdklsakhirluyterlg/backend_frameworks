from django.urls import path
from . import views
from pathlib import Path

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
