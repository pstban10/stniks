from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('clases.urls')),
    path('user/', include('data.urls')),
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls, name='admin'),
]
