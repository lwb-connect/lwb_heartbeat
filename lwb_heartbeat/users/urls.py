"""Imports."""
from django.urls import path
from .views import UserView


urlpatterns = [
    path('', UserView.as_view(), name='user'),
    # path('<str:username>', ProfileView.as_view(), name='named_profile'),
    # path('edit/', ProfileEditView.as_view(), name='profile_edit'),
]