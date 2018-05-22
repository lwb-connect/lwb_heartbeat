from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView


class StaffView(LoginRequiredMixin, DetailView):
    pass