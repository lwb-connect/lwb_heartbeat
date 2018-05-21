from django.urls import path
from .views import (
    ChildDetailView,
    ChildCreateView)


urlpatterns = [
    path('childs/<int:pk>', ChildDetailView.as_view(), name='child_detail'),
    path('childs/add', ChildCreateView.as_view(), name='child_create'),