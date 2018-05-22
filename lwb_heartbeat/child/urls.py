from django.urls import path
from .views import (
    ChildDetailView,
    ChildCreateView)


urlpatterns = [
    path('child/<int:pk>', ChildDetailView.as_view(), name='child_detail'),
    path('child/add', ChildCreateView.as_view(), name='child_create'),
    ] 
     