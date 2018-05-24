from django.db import models
from django.contrib.auth.models import User
from sorl.thumbnail import ImageField
from child.models import Child


class Photo(models.Model):
    """
    Creates Photo model that is associated with a single child.
    """
    child = models.ForeignKey(
        Child,
        on_delete=models.CASCADE,
        related_name='photos'
        )
    image = ImageField(upload_to='images')
    # location = models.CharField(max_length=250, default='none', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    date_uploaded = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)
    # published = models.CharField(
    #     max_length=250,
    #     choices=(
    #         ('PRIVATE', 'Private'),
    #         ('SHARED', 'Shared'),
    #         ('PUBLIC', 'Public'),
    #     )
    # )

    def __str__(self):
        """Returns representation of current Photo title."""
        return '{}: {}'.format(self.child, self.description)
