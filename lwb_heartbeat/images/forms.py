"""Imports."""
from django.forms import ModelForm
from .models import Photo


class PhotoForm(ModelForm):
    """Lets the agent add photos."""

    class Meta:
        """Meta class."""

        model = Photo
        fields = ['image', 'description']

    def __init__(self, *args, **kwargs):
        """Init method."""
        username = kwargs.pop('username')
        super().__init__(*args, **kwargs)


class PhotoEditForm(ModelForm):
    """Lets the agent edit photo information."""

    class Meta:
        """Meta class."""

        model = Photo
        fields = ['image', 'description']

    def __init__(self, *args, **kwargs):
        """Init method."""
        super().__init__(*args, **kwargs)
        username = kwargs.pop('username')
