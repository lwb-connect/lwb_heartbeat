from django.urls import path
from .views import ChildDetailView, ChildCreateView, ChildListView, ChildEditView, ChildMedicalUpdateView


urlpatterns = [
    path('childlist', ChildListView.as_view(), name='childlist'),
    path('child/<int:pk>', ChildDetailView.as_view(), name='child_detail'),
    path('child/add', ChildCreateView.as_view(), name='child_create'),
    path('childsettings/<int:pk>', ChildEditView.as_view(),
         name='childsettings'),
    path('medicalchart/<int:pk>', ChildMedicalUpdateView.as_view(), name='medicalchart')
    ]
