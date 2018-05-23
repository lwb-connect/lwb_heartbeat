"""Imports."""
from django.urls import path
from .views import ProfileView, ProfileEditView, StaffListView
from .models import StaffProfile

urlpatterns = [
    path('stafflist', StaffListView.as_view(), name='stafflist'),
    path('', ProfileView.as_view(), name='profile'),
    path('<str:username>', ProfileView.as_view(), name='named_profile'),
    path('settings/<str:username>', ProfileEditView.as_view(),
         name='settings'),
    ]
