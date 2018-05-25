from django.views.generic import (TemplateView, ListView,
                                  DetailView, CreateView, UpdateView)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.conf import settings
from .forms import ChildEditForm, ChildAddForm
from .models import Child, MedicalUpdate
from images.models import Photo
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


class ChildMedicalUpdateView(LoginRequiredMixin, DetailView):
    template_name = 'child_medical_veiw.html'
    model = MedicalUpdate
    login_url = reverse_lazy('auth_url')
    context_object_name = 'medicalupdate'

    def get_queryset(self):
        return MedicalUpdate.objects.filter(child__id=self.kwargs['pk'])

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['child'] = Child.objects.filter(id=self.kwargs['pk']).first()
        context['medicalupdate'] = self.get_queryset()
        return context
# 


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
        # form.instance.user = self.request.user
        # form.instance.save()
        # import pdb; pdb.set_trace()
        photo = form.instance.photos.first()
        if photo and 'image' not in form.files:
            photo.delete()
        elif photo:
            photo.image = form.files['image']
            photo.description = form.data['description']
            photo.save()
        elif 'image' in form.files:
            # create new photo instance
            photo = Photo(
                child=form.instance,
                image=form.files['image'],
                description=form.data['description']
            )
            photo.save()

        return super().form_valid(form)


class ChildDetailView(LoginRequiredMixin, DetailView):
    template_name = 'child_profile.html'
    model = Child
    login_url = reverse_lazy('auth_url')
    pk_url_kwarg = 'pk'

    # DON'T DELETE
    # NEED FOR REFERENCE ----------------------------------------

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)

    #     # photos = Photo.objects.filter(user__username=self.request.user.username)
    #     # import pdb; pdb.set_trace()
    #     # context['child_photos'] = photos

    #     return context

    # def get_queryset(self):
    #     return Child.objects.filter(published='PUBLIC')
    # -------------------------------------------------------------

class ChildCreateView(LoginRequiredMixin, CreateView):
    """Lets a staff with appropriate permissions add a child to the system."""
    pass
    template_name = 'child_create.html'
    model = Child
    form_class = ChildAddForm
    success_url = reverse_lazy('childlist')
    login_url = reverse_lazy('auth_login')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'username': self.request.user.username})
        return kwargs

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.save()
        if 'image' in form.files:
            # create new photo instance
            photo = Photo(
                child=form.instance,
                image=form.files['image'],
                description=form.data['description']
            )
            photo.save()

        return super().form_valid(form)
