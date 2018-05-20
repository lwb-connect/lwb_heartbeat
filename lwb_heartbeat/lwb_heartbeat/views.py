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


# class HomeView(TemplateView):
#     """Routes user to home view page."""
#     template_name = 'generic/home.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         # photos = Photo.objects.filter(published='PUBLIC')

#         # if photos.count():
#         #     image = photos.order_by('?').first()
#         #     image_url = image.image

#         # else:
#         #     image_url = 'http://via.placeholder.com/250x250'
#         #     image_title = 'Placeholder'

#         # context['image_url'] = image_url
#         context['message'] = 'Hello World'

#         return context
