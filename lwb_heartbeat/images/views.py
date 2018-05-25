from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from django.views.generic.edit import FormView
from images.models import Photo
# from imager_profile.models import ImagerProfile
from .forms import PhotoForm, PhotoEditForm
from django.conf import settings


# class PhotoView(ListView):
#     """Displays all images from a specified child"""
#     # DO
#     template_name = ''
#     context_object_name = 'photo'

#     def get(self, *args, **kwargs):
#         # DO
#         # view tiers here
#         # maybe
#         if not self.request.user.is_authenticated:
#             return redirect('home')
#         return super().get(*args, **kwargs)

#     def get_queryset(self):
#         return Photo.objects.filter(published='PUBLIC')

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         return context


class PhotoCreateView(LoginRequiredMixin, CreateView):
    """Lets a user add a photo to a child"""
    # DO
    template_name = ''
    login_url = reverse_lazy('auth_login')
    # form_class = PhotoForm
    # DO
    # change
    success_url = reverse_lazy('library')
    model = Photo

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        # DO
        # reference child, not user
        kwargs.update({'username': self.request.user.username})
        return kwargs

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PhotoEditView(LoginRequiredMixin, UpdateView):
    """Lets agents edit existing photo information."""
    # DO
    template_name = ""
    model = Photo
    form_class = PhotoEditForm
    login_url = reverse_lazy('auth_login')
    success_url = reverse_lazy('photo')
    slug_url_kwarg = 'photo_id'
    slug_field = 'id'

    # DO
    # reference child, not user
    def get(self, *args, **kwargs):
        self.kwargs['username'] = self.request.user.get_username()
        return super().get(*args, **kwargs)

    def post(self, *args, **kwargs):
        self.kwargs['username'] = self.request.user.get_username()
        return super().post(*args, **kwargs)

    def form_valid(self, form):
        form.instance.title = form.data['title']
        form.instance.save()
        return super().form_valid(form)
