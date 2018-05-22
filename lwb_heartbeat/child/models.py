from django.db import models
from django.contrib.auth.models import User
from sorl.thumbnail import ImageField


class Child(models.Model):
    child = models.ForeignKey(User, on_delete=models.CASCADE, related_name='childs')
    child_id = models.ForeignKey('Photo', on_delete=models.SET_NULL, related_name='+', null=True, blank=True)
    nick_name = models.CharField(max_length=180, default='Untitled')
    given_name = models.CharField(max_length=180, default='Untitled')
    d_o_b = models.DateField(blank=True, null=True)
    date_modified = models.DateField(auto_now=True)
    published = models.CharField(
        max_length=7,
        choices=(
            ('PRIVATE', 'Private'),
            ('SHARED', 'Shared'),
            ('PUBLIC', 'Public'),
        )
    )

    def __str__(self):
        return '{}'.format(self.name)


