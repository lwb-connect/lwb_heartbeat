"""Imports."""
from django.urls import path
from .views import StaffView


urlpatterns = [
    path('', StaffView.as_view(), name='staff'),
    # path('<str:username>', ProfileView.as_view(), name='named_profile'),
    # path('edit/', ProfileEditView.as_view(), name='profile_edit'),
]