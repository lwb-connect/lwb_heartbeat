from django.forms import ModelForm
from .models import Photo


class PhotoForm(ModelForm):
    """Lets the user add photos"""
    class Meta:
        model = Photo
        fields = ['image', 'title', 'description']

    def __init__(self, *args, **kwargs):
        username = kwargs.pop('username')
        super().__init__(*args, **kwargs)

        self.fields['image'].queryset = Photo.objects.filter(
                                        user__username=username)
