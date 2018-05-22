from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField


class Child(models.Model):
    """
    Defines the model in whicha Child in LWB care will be defined.
    """
    child = models.ForeignKey(User, on_delete=models.CASCADE, related_name='child')
    program_number = models.CharField(
        default='CSB000001',
        max_length=9, 
        null=True, 
        blank=True,
        )
    nick_name = models.CharField(max_length=180, default='Untitled')
    given_name = models.CharField(max_length=180, default='Untitled')
    d_o_b = models.DateField(blank=True, null=True)
    date_modified = models.DateField(auto_now=True)
    location_country = models.CharField(
        max_length=8,
        blank=True, 
        null=True,
        choices=(
            ('CAMBODIA', 'cambodia'),
            ('CHINA', 'china'),
            ('INDIA', 'india'),
            ('UGANDA', 'uganda'),
        ))
    # program = models.ForeignKey(
    #     Program, 
    #     on_delete=models.CASCADE, 
    #     related_name='child'
    #     )

    def __str__(self):
        return '{}'.format(self.program_number)


class Program(models.Model):
    """
    Defines the programs to which a Child instance can be related.
    """
    child = models.ForeignKey(
        Child, 
        on_delete=models.CASCADE, 
        related_name='program'
        )
    program = MultiSelectField(
        blank=True, 
        null=True,
        choices=(('CAM_BIM_RANGSEI_VILLAGE',
                  'cam_bim_rangsei_village'),
                 ('CAM_BIM_SOKHEM_VILLAGE',
                  'cam_bim_sokhem_village'),
                 ('CAM_BIM_ARY_VILLAGE',
                  'cam_bim_ary_village'),
                 ('CAM_SIB_SOKHEM_VILLAGE',
                  'cam_sib_sokhem_village'),
                 ))
