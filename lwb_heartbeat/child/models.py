from django.db import models
from multiselectfield import MultiSelectField
from staff.models import StaffProfile
# from django.contrib.auth.models import User


class Country(models.Model):
    """
    Defines the Countries in the LWB Organization.  
    """
    lwbprogram = models.ForeignKey(
        'LWBProgram', 
        on_delete=models.PROTECT, 
        null=True,
        blank=True,
        )
    staff = models.ForeignKey(
        StaffProfile, 
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        )
    children = models.ForeignKey(
        'Child', 
        on_delete=models.PROTECT, 
        null=True,
        blank=True,
        )
    country_name = models.CharField(max_length=30, unique=True)


class Child(models.Model):
    """
    Defines the model in whicha Child in LWB care will be defined.
    """
    program_number = models.CharField(
        default='CSB000001',
        max_length=9, 
        null=True, 
        blank=True,
        unique=True,
        )
    nick_name = models.CharField(max_length=180, default='Untitled')
    given_name = models.CharField(max_length=180, default='Untitled')
    d_o_b = models.DateField(blank=True, null=True)
    date_modified = models.DateField(auto_now=True)
    location_country = models.ForeignKey(
        Country, 
        on_delete='CASCADE'
        )
    # program = models.ForeignKey(
    #     'Program', 
    #     blank=True, 
    #     null=True,
    #     on_delete=models.CASCADE, 
    #     related_name='child'
    #     )
    # medical_code = models.ForeignKey(
    #     'MedicalCodes', 
    #     on_delete=models.CASCADE, 
    #     related_name='child'
    #     )

    def __str__(self):
        return '{}'.format(self.program_number)


class LWBProgram(models.Model):
    """
    Defines the programs to which a Child instance can be related.
    """
    child = models.OneToOneField(
        Child,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name='lwbprogram'
    )
    lwbprogram = MultiSelectField(
        max_length=240,
        blank=True, 
        null=True,
        choices=(
            ('ED', 'Education'),
            ('FC', 'Foster Care'),
            ('MD', 'Medical'),
            ('TF', 'Traffic Rescue')
        ))


class Education(models.Model):
    """
    Defines all the Education programs in the LWB Organization.  
    """
    country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE)
    school = MultiSelectField(
        choices=(('ED_CAM_BIM_RANGSEI_VILLAGE',
                  'ED Cambodia Rangsei Village BIM'),
                 ('ED_CAM_BIM_SOKHEM_VILLAGE',
                  'ED Cambodia Sokhem Village BIM'),
                 ('ED_CAM_BIM_ARY_VILLAGE',
                  'ED Cambodia Ary Village BIM'),
                 ('ED_CAM_SIB_SOKHEM_VILLAGE',
                  'ED Cambodia Sokhem Village Sibling School'), 
                 ))


class MedicalCodes(models.Model):
    """
    Defines the programs to which a Child instance can be related.
    """
    child = models.OneToOneField(
        Child,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name='medical_codes'
        )

    medical_codes = MultiSelectField(
        max_length=240,
        blank=True, 
        null=True,
        choices=(
            ('AA', 'AA Anal Atresia'),
            ('AB', 'AB Amniotonic Banding'),
            ('AN', 'AN Animal Injury'),
            ('AU', 'AU Auditory Issues'),
            ('BA', 'BA Biliary Atresia'),
            ('BE', 'BE Bladder Extrophy'),
            ('BI', 'BI Burn Injury'),
            ('BL', 'BL Blood Issues'),
            ('CA', 'CA Cancer'),
            ('CF', 'CF Club Feet'),
            ('CH', 'CH Club Hands'),
            ('CJ', 'CJ Conjoined Twins'),
            ('CL', 'CL Cleft Lip'),
            ('CP', 'CP Cleft Palate'),
            ('EA', 'EA Esophageal Atresia'),
            ('EV', 'EV Evaluation'),
            ('EY', 'EY Eye Issues'),
            ('FT', 'FT Failure to Thrive'),
            ('GE', 'GE Genital Issues'),
            ('GI', 'GI Gastrointestinal'),
            ('GS', 'GS General Sergery'),
            ('HE', 'HE Hernia Surgery'),
            ('HM', 'HM Hemangioma Surgery'),
            ('HT', 'HT Heart Surgery'),
            ('IF', 'IF Infection Treatment'),
            ('IJ', 'IJ Injury'),
            ('MT', 'MT Medical Testing'),
            ('NE', 'NE Neurologic Issues'),
            ('OR', 'OR Orthopedic Issues'),
            ('PN', 'PN Pneumonia Treatment'),
            ('PR', 'PR Premature Newbord Care'),
            ('PT', 'PT Physical Therapy'),
            ('PU', 'PU Pulmonary Issues'),
            ('RI', 'RI Renal Issues'),
            ('TU', 'TU Tumors (ex. Teratomas'),
            ('UR', 'UR Urologic Issues'),  
            ))
