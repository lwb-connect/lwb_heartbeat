"""Imports."""
from django.urls import reverse, reverse_lazy
from django.shortcuts import render


def home_view(request):
    """Home view."""
    return render(request, 'generic/home.html', {})


def about_us_view(request):
    """About us view."""
    return render(request, 'generic/about_us.html', {})
