from django.views.generic import (TemplateView, ListView,
                                  DetailView, CreateView, UpdateView)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.conf import settings
from .forms import ChildEditForm
from .models import Child
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect


class ChildListView(LoginRequiredMixin, ListView):
    """View to see a list of all children."""

    template_name = "child_list.html"
    login_url = reverse_lazy('auth_login')
    context_object_name = 'children'
    model = Child

    def get(self, *args, **kwargs):
        """get args and kwargs"""

        return super().get(*args, **kwargs)

    def get_context_data(self, **kwargs):
        """return context data"""
        context = super().get_context_data(**kwargs)
        return context

# OLD VERSION:------------------------------------------------------
# don't delete until presentation

# class ChildEditView(LoginRequiredMixin, UpdateView):
#     """Lets admin or super edit a child profile."""

#     template_name = 'child_edit.html'
#     model = Child
#     form_class = ChildEditForm
#     login_url = reverse_lazy('auth_login')
#     success_url = reverse_lazy('children')
#     # DO
#     # change to use pk
#     slug_url_kwarg = 'username'
#     slug_field = 'user__username'

#     def get(self, *args, **kwargs):
#         """Get."""
#         self.kwargs['username'] = self.request.user.get_username()
#         return super().get(*args, **kwargs)

#     def post(self, *args, **kwargs):
#         """Post."""
#         self.kwargs['username'] = self.request.user.get_username()
#         return super().post(*args, **kwargs)

#     def get_form_kwargs(self):
#         """Get kwargs."""
#         kwargs = super().get_form_kwargs()
#         kwargs.update({'username': self.request.user.get_username()})
#         return kwargs

#     def form_valid(self, form):
#         """Validate form."""
#         # form.instance.user.email = form.data['email']
#         form.instance.user.first_name = form.data['first_name']
#         form.instance.user.last_name = form.data['last_name']
#         form.instance.user.save()
#         return super().form_valid(form)


class ChildEditView(LoginRequiredMixin, UpdateView):
    """Lets admin or super edit a child profile."""

    template_name = 'child_edit.html'
    model = Child
    form_class = ChildEditForm
    login_url = reverse_lazy('auth_login')
    success_url = reverse_lazy('childlist')

    def get(self, *args, **kwargs):
        """Get info"""
        # DO
        # maybe only need return super
        self.kwargs['username'] = self.request.user.get_username()
        return super().post(*args, **kwargs)

    def post(self, *args, **kwargs):
        """Post for child edit form."""
        # Do
        # same as the get comment
        self.kwargs['username'] = self.request.user.get_username()
        return super().post(*args, **kwargs)

    def get_form_kwargs(self):
        """Get kwargs from edit form."""
        kwargs = super().get_form_kwargs()
        kwargs.update({'username': self.request.user.get_username()})
        return kwargs

    def form_valid(self, form):
        """Validate form data."""
        form.instance.user = self.request.user
        # DO
        # maybe use, with child instead of user......
        # form.instance.user.save()
        return super().form_valid(form)


class ChildDetailView(LoginRequiredMixin, DetailView):
    template_name = 'child_profile.html'
    model = Child
    login_url = reverse_lazy('auth_url')
    pk_url_kwarg = 'pk'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    # def get_queryset(self):
    #     return Child.objects.filter(published='PUBLIC')


class ChildCreateView(LoginRequiredMixin, CreateView):
    pass
    # template_name = 'child_create.html'
    # model = Child
    # form_class = ChildForm
    # success_url = 'store'
    # login_url = reverse_lazy('auth_login')

    # def get_form_kwargs(self):
    #     kwargs = super().get_form_kwargs()
    #     kwargs.update({'username': self.request.user.username})
    #     return kwargs

    # def form_valid(self, form):
    #     form.instance.user = self.request.user
    #     return super().form_valid(form)