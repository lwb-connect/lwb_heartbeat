from django.db import models
from django.contrib.auth.models import User


class Child(models.Model):
    # child = models.ForeignKey(User, on_delete=models.CASCADE, related_name='child')
    child_id = models.AutoField(primary_key=True),
    program_number = models.CharField(
        default='CSB###176',
        max_length=9, 
        null=True, 
        blank=True,
        ),
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
        return '{}'.format(self.child_id)


