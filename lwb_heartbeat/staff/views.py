"""Imports."""
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView, TemplateView, ListView
from .models import StaffProfile
from .forms import ProfileEditForm


class ProfileView(LoginRequiredMixin, TemplateView):
    """Profile view class."""

    template_name = 'profile.html'
    login_url = reverse_lazy('auth_login')
    model = StaffProfile
    context_object_name = 'profile'

    def get(self, *args, **kwargs):
        """Get username."""
        if kwargs:
            return super().get(*args, **kwargs)

        else:
            kwargs.update({'username': self.request.user.username})

        return super().get(*args, **kwargs)

    def get_context_data(self, **kwargs):
        """Get context data for profiles."""
        context = super().get_context_data(**kwargs)
        profile = get_object_or_404(
            StaffProfile, user__username=context['username'])

        context['profile'] = profile
        return context


class ProfileEditView(LoginRequiredMixin, UpdateView):
    """Lets the user edit their profile."""

    template_name = 'profile_edit.html'
    model = StaffProfile
    form_class = ProfileEditForm
    login_url = reverse_lazy('auth_login')
    success_url = reverse_lazy('profile')
    slug_url_kwarg = 'username'
    slug_field = 'user__username'

    def get(self, *args, **kwargs):
        """Get."""
        self.kwargs['username'] = self.request.user.get_username()
        return super().get(*args, **kwargs)

    def post(self, *args, **kwargs):
        """Post."""
        self.kwargs['username'] = self.request.user.get_username()
        return super().post(*args, **kwargs)

    def get_form_kwargs(self):
        """Get kwargs."""
        kwargs = super().get_form_kwargs()
        kwargs.update({'username': self.request.user.get_username()})
        return kwargs

    def form_valid(self, form):
        """Validate form."""
        form.instance.user.email = form.data['email']
        form.instance.user.first_name = form.data['first_name']
        form.instance.user.last_name = form.data['last_name']
        form.instance.user.save()
        return super().form_valid(form)


class StaffListView(LoginRequiredMixin, ListView):
    """Staff List view."""

    template_name = 'staff_list.html'
    login_url = reverse_lazy('auth_login')
    context_object_name = 'profile'
    model = StaffProfile

    def get(self, *args, **kwargs):
        """Get username."""
        if kwargs:
            return super().get(*args, **kwargs)

        else:
            kwargs.update({'username': self.request.user.username})

        return super().get(*args, **kwargs)

    def get_context_data(self, **kwargs):
        """Get context."""
        context = super().get_context_data(**kwargs)
        return context
