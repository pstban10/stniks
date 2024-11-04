from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='inicio'),
    path('horarios/', views.horarios, name='horarios'),
    path('reservar', views.clase_de_prueba, name='reservar'),
    path('ver_horarios/', views.ver_horarios, name='ver_horarios'),

]
