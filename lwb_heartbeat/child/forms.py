from django.forms import ModelForm
from .models import Child, Photo


class ChildForm(ModelForm):
    class Meta:
        model = Child
        fields = ['child_id', 'nick_name', 'given_name', 'D_O_B', 'facility']

    def __init__(self, *args, **kwargs):
        username = kwargs.pop('username')
        super().__init__(*args, **kwargs)
        self.fields['child_id'].queryset = Photo.objects.filter(child__user__username=username)