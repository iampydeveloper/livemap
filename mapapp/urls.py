#mapapp/urls.py
# urls.py

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.map_view, name='map'),
    path('get_markers/', views.get_markers, name='get_markers'),
    path('add_marker/', views.add_marker, name='add_marker'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
