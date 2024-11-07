from django.urls import path
from . import views

urlpatterns = [
    path('profile', views.profile, name='profile'),
    path('records', views.RecordsListView.as_view(), name='records'),
    path('records/edit/<int:pk>', views.edit_record, name='edit_record'),

]
