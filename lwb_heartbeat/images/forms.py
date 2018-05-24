from django.forms import ModelForm
from .models import Photo


# DO
# Filter by child, not username

class PhotoForm(ModelForm):
    """Lets the agent add photos"""
    class Meta:
        model = Photo
        fields = ['image', 'description']

    def __init__(self, *args, **kwargs):
        username = kwargs.pop('username')
        super().__init__(*args, **kwargs)

        # self.fields['image'].queryset = Photo.objects.filter(
        #                                 user__username=username)


class PhotoEditForm(ModelForm):
    """Lets the agent edit photo information."""
    class Meta:
        model = Photo
        fields = ['image', 'description']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        username = kwargs.pop('username')
