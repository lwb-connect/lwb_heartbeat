from django.urls import path
from .views import PhotoCreateView, PhotoEditView

urlpatterns = [
    # path("photo", PhotoView.as_view(), name="photo"),
    path("photo/add", PhotoCreateView.as_view(), name="photo_create"),
    path('photosettings/<int:pk>', PhotoEditView.as_view(),
         name='photosettings'),
]