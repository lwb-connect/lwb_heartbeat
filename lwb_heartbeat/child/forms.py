"""imports."""
from django.contrib.auth.models import User
from django.forms import ModelForm, CharField
from .models import Child, Country


class ChildEditForm(ModelForm):
    """Form for editing/updating child information."""

    # DO
    # maybe no need
    country_name = CharField(
        # lets you get meta data of another model
        max_length=Country._meta.get_field('country_name').max_length,)

    class Meta:
        model = Child
        fields = ['currently_in_lwb_care', 'date_entered_lwb_care',
                  'date_child_left_lwb_care', 'program_number',
                  'nick_name', 'given_name_sur', 'given_name_first', 'DOB',
                  'location_country', 'education_program']

    def __init__(self, *args, **kwargs):
        """Initialization."""
        username = kwargs.pop('username')
        # super().__init__(*args, **kwargs)
        # # self.fields['child_id'].queryset = Child.objects.filter(child__user__username=username)
        # self.fields['country_name'].initial = Country.objects.get(
        #                                         username=username).country_name
        super().__init__(*args, **kwargs)


class ChildAddForm(ModelForm):
    """Form for adding a child to the database."""

    class Meta:
        """Add metadata"""
        model = Child
        # DO
        fields = []

    def __init__(self, *args, **kwargs):
        """Initialization."""
        kwargs.pop('username')
        super().__init__(*args, **kwargs)
