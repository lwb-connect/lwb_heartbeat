"""Imports."""
from django.urls import path
from .views import ProfileView, ProfileEditView
from .models import StaffProfile

urlpatterns = [
    path('', ProfileView.as_view(), name='profile'),
    path('<str:username>', ProfileView.as_view(), name='named_profile'),
    path('settings/<str:username>', ProfileEditView.as_view(), name='settings')
]