# from django.views.generic import TemplateView
# from imager_images.models import Photo
from django.urls import reverse, reverse_lazy
from django.shortcuts import render


def home_view(request):
    """ home view."""
    return render(request, 'generic/home.html', {})


# class HomeView(TemplateView):
#     """Home view class."""

#     template_name = 'generic/home.html'

#     def get_context_data(self, *args, **kwargs):
#         """Home view."""
#         context = super().get_context_data(**kwargs)
#         # context['background'] = sample(list(Photo.objects.filter(published="PUBLIC")) + [None], 1)[0]
#         context['message'] = 'Hello World'

#         return context


