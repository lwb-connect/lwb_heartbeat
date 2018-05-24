from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.conf import settings
# from .forms import ChildForm
from .models import Child


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


class ChildDetailView(LoginRequiredMixin, DetailView):
    template_name = 'child_detail.html'
    model = Child
    login_url = reverse_lazy('auth_url')
    pk_url_kwarg = 'pk'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self):
        return Child.objects.filter(published='PUBLIC')


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