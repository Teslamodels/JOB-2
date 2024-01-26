from django.urls import path
from .views import get_data, create_data, update_data, delete_data

urlpatterns = [
    path('data/', get_data, name='data'),
    path('new/data/', create_data, name='create'),
    path('edit/<slug:slug>/', update_data, name='edit'),
    path('delete/<slug:slug>/', delete_data, name='delete'),
]