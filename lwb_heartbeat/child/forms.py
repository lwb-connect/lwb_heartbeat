"""imports."""
from django.contrib.auth.models import User
from django.forms import ModelForm, CharField, ImageField, Textarea, widgets
from .models import Child, Country
from images.models import Photo
# don't use
# from sorl.thumbnail import ImageField


class ChildEditForm(ModelForm):
    """Form for editing/updating child information."""

    # DO
    # maybe no need

    # country_name = CharField(
    #     # lets you get meta data of another model
    #     max_length=Country._meta.get_field('country_name').max_length,)
    image = ImageField(required=False)
    description = CharField(widget=Textarea, required=False)

    class Meta:
        model = Child
        fields = ['currently_in_lwb_care', 'date_entered_lwb_care',
                  'date_child_left_lwb_care', 'program_number',
                  'nick_name', 'given_name_sur', 'given_name_first', 'DOB',
                  'location_country', 'education_program',
                  'image', 'description']

    def __init__(self, *args, **kwargs):
        """Initialization."""
        username = kwargs.pop('username')

        # # self.fields['child_id'].queryset = Child.objects.filter(child__user__username=username)
        # self.fields['country_name'].initial = Country.objects.get(
        #                                         username=username).country_name
        super().__init__(*args, **kwargs)
        photo = self.instance.photos.first()
        # import pdb; pdb.set_trace()
        if photo:
            self.fields['image'].initial = photo.image
            self.fields['description'].initial = photo.description


class ChildAddForm(ModelForm):
    """Form for adding a child to the database."""

    image = ImageField(required=False)
    description = CharField(widget=Textarea, required=False)

    class Meta:
        """Add metadata"""
        model = Child
        # DO
        fields = ['currently_in_lwb_care', 'date_entered_lwb_care',
                  'date_child_left_lwb_care', 'program_number',
                  'nick_name', 'given_name_sur', 'given_name_first', 'DOB',
                  'location_country', 'education_program',
                  'image', 'description']

    def __init__(self, *args, **kwargs):
        """Initialization."""
        kwargs.pop('username')
        super().__init__(*args, **kwargs)
