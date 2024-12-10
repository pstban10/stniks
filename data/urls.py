from django.urls import path
from . import views

urlpatterns = [
    path('profile', views.profile, name='profile'),
    path('records', views.RecordsListView.as_view(), name='records'),
    path('filter_records/', views.filter_records, name='filter_records'),
    path('add_user', views.add_user, name='add_user'),
    path('add_record', views.add_record, name='add_record'),
    path('records/edit/<int:pk>', views.edit_record, name='edit_record'),
]
