from django.db import models
from django.contrib.auth.models import User
from sorl.thumbnail import ImageField
# import child model


# class Albums(models.Model):
#     """
#     Creates Album model with CHILD as it's ForeignKey.
#     Albums is truncated if user is deleted from table.
#     """
#     child = models.ForeignKey(User, on_delete=models.CASCADE, related_name='albums')
#     photos = models.ManyToManyField('Photo', related_name='albums')
#     cover = models.ForeignKey('Photo', on_delete=models.SET_NULL, related_name='+', null=True, blank=True)
#     title = models.CharField(max_length=180, default='Untitled')
#     description = models.TextField(blank=True, null=True)
#     # price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
#     date_created = models.DateField(auto_now_add=True)
#     date_modified = models.DateField(auto_now=True)
#     date_published = models.DateField(blank=True, null=True)
#     # published = models.CharField(
#     #     max_length=7,
#     #     choices=(
#     #         ('PRIVATE', 'Private'),
#     #         ('SHARED', 'Shared'),
#     #         ('PUBLIC', 'Public'),
#     #     )
#     # )

#     def __str__(self):
#         """Returns representation of current Album title."""
#         return '{}'.format(self.title)

class Photo(models.Model):
    """
    Creates Photo model that uses one way connection to Album to join both
    tables to build assocation stream.
    """
    child = models.ForeignKey(Child, on_delete=models.CASCADE, related_name='photos')
    image = ImageField(upload_to='images')
    title = models.CharField(max_length=250, default='Untitled')
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
        return '{}'.format(self.title)
