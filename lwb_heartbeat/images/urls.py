from django.urls import path
from .views import PhotoView, PhotoCreateView

urlpatterns = [
    path("photo", PhotoView.as_view(), name="photo"),
    path("photo/add", PhotoCreateView.as_view(), name="photo_create"),
]
