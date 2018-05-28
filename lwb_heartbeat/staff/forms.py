"""imports."""
from django.contrib.auth.models import User
from .models import StaffProfile
from django.forms import ModelForm, CharField, widgets


class ProfileEditForm(ModelForm):
    """Edit form class."""

    # username =
    email = CharField(
        # lets you get meta data of another model
        max_length=User._meta.get_field('email').max_length,
        widget=widgets.EmailInput(),
    )
    first_name = CharField(
        max_length=User._meta.get_field('first_name').max_length,
        required=False,
    )
    last_name = CharField(
        max_length=User._meta.get_field('last_name').max_length,
        required=False,
    )

    class Meta:
        """Meta class."""

        model = StaffProfile
        fields = [
            'first_name', 'last_name', 'about_you', 'country_of_residence', 'city_of_residence', 'email', 'phone', 'location', 'user_language_spoken', 'user_language_spoken_other', 'user_language_written', 'user_language_written_other']

    def __init__(self, *args, **kwargs):
        username = kwargs.pop('username')
        super().__init__(*args, **kwargs)
        self.fields['email'].initial = User.objects.get(
                                                username=username).email
        self.fields['first_name'].initial = User.objects.get(
                                                username=username).first_name
        self.fields['last_name'].initial = User.objects.get(
                                                username=username).last_name
