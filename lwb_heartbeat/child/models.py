from django.db import models
from multiselectfield import MultiSelectField

# caution:
# infinite loop import:
# from images.models import Photo
from sorl.thumbnail import ImageField


class Country(models.Model):
    """
    Defines the Countries in the LWB Organization.
    """
    class Meta:
        verbose_name_plural = "Countries"

    country_name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.country_name


class Child(models.Model):
    """
    Defines the model in whicha Child in LWB care will be defined.
    """
    class Meta:
        verbose_name_plural = "Children"

    currently_in_lwb_care = models.BooleanField(default=True)
    date_entered_lwb_care = models.DateField(blank=True, null=True)
    date_child_left_lwb_care = models.DateField(blank=True, null=True)
    program_number = models.CharField(
        default='CSB000001',
        max_length=9,
        null=True,
        blank=True,
        unique=True,
        )
    nick_name = models.CharField(max_length=180, default='nick name')
    given_name_sur = models.CharField(max_length=180, default='sur name')
    given_name_first = models.CharField(max_length=180, default='first name')
    DOB = models.DateField(blank=True, null=True)
    date_modified = models.DateField(auto_now=True)
    location_country = models.ForeignKey(
        Country,
        on_delete='CASCADE',
        related_name='children',
        null=True,
        blank=True,
        )
    education_program = models.ForeignKey(
        'Education',
        on_delete='CASCADE',
        related_name='children',
        null=True,
        blank=True,
        )

    def __str__(self):
        return '{}, {}, {}, {}'.format(
            self.program_number,
            self.nick_name,
            self.given_name_sur,
            self.given_name_first
            )


class GrowthData(models.Model):
    """
    Defines growth data for child updates
    """
    class Meta:
        verbose_name_plural = "Growth Data"

    child = models.ForeignKey(
        Child,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        )
    date_recorded = models.DateField(auto_now=True)
    height_cm = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        blank=True,
        null=True,
        )
    weight_kg = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        blank=True,
        null=True,
        )

    @property
    def bmi(self):
        """
        Calculates and returns bmi.
        """
        return self.weight_kg / (self.height_cm * 100)**2

    concern_flag = models.BooleanField(default=False)

    def __str__(self):
        return '{}, Conern: {}'.format(self.child, self.concern_flag)


class GeneralUpdate(models.Model):
    """
    Handles general text reports and notes on a Child instance.
    """
    class Meta:
        verbose_name_plural = "General Updates"

    child = models.ForeignKey(
        Child,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        )
    date_created = models.DateField(auto_now=True)
    note = models.CharField(max_length=10000, default='enter child notes here')


class MedicalUpdate(models.Model):
    """
    Handles medical text reports and notes on a Child instance.
    """
    class Meta:
        verbose_name_plural = "Medical Updates"

    child = models.ForeignKey(
        Child,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name='medical_update'
        )
    date_created = models.DateField(auto_now=True)
    date_edited = models.DateField(auto_now=False)
    medical_note = models.CharField(
        max_length=10000,
        null=True,
        blank=True,
        default='enter child notes here'
        )


class LWBProgram(models.Model):
    """
    Defines the programs to which a Child instance can be related.
    """
    class Meta:
        verbose_name_plural = "LWB Programs"

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
            ('TF', 'Safe Haven'),
            ('NT', 'Nutrition'),
            ('HH', 'Healing Home')
        ))
    country = models.ManyToManyField(
            Country,
            blank=True,
            related_name='lwbprogram'
        )

    def __str__(self):
        return '{}'.format(self.lwbprogram)


class Education(models.Model):
    """
    Defines all the Education programs in the LWB Organization.
    """
    class Meta:
        verbose_name_plural = "Education Programs"

    education_program = models.ForeignKey(
        LWBProgram,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name='education_program'
        )
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

    def __str__(self):
        return str(self.school)


class FosterCare(models.Model):
    """
    Defines all the Foster programs in the LWB Organization.
    """
    class Meta:
        verbose_name_plural = "Foster Care Programs"

    foster_program = models.ForeignKey(
        LWBProgram,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name='foster_care'
        )
    location = MultiSelectField(
        choices=(
            ('N/A', 'Not Currently Available'),
            ('N/A', 'Not Currently Available'),
            ))

    def __str__(self):
        return str(self.foster_program)


class HealingHome(models.Model):
    """
    Defines all the Foster programs in the LWB Organization.
    """
    class Meta:
        verbose_name_plural = "Healing Home Programs"

    healing_home_program = models.ForeignKey(
        LWBProgram,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name='healing_home'
        )
    healing_home_id = MultiSelectField(
        choices=(
            ('N/A', 'Not Currently Available'),
            ))

    def __str__(self):
        return str(self.healing_home_id)


class Trafficking(models.Model):
    """
    Defines all the human trafficking aid programs in the LWB Organization.
    """
    class Meta:
        verbose_name_plural = "Trafficking Programs"

    trafficking_program = models.ForeignKey(
        LWBProgram,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name='trafficking_program')
    trfk_program_id = MultiSelectField(
        choices=(
            ('N/A', 'Not Currently Available'),
            ))

    def __str__(self):
        return str(self.trfk_program_id)


class Medical(models.Model):
    """
    Defines all the medical programs in the LWB Organization.
    """
    class Meta:
        verbose_name_plural = "Medical Programs"

    medical_program = models.ForeignKey(
        LWBProgram,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name='medical_program')
    location = MultiSelectField(
        choices=(
            ('KSFH', 'Khmer-Soviet Friendship Hospital'),
            ))

    def __str__(self):
        return str(self.location)


class Nutrition(models.Model):
    """
    Defines all the human trafficking aid programs in the LWB Organization.
    """
    class Meta:
        verbose_name_plural = "Nutrition Programs"

    nutrition_program = models.ForeignKey(
        LWBProgram,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name='nutrition_program'
        )
    nutr_id = MultiSelectField(
        choices=(
            ('N/A', 'Not Currently Available'),
            ))

    def __str__(self):
        return str(self.nutr_id)


class MedicalCodes(models.Model):
    """
    Defines the programs to which a Child instance can be related.
    """
    class Meta:
        verbose_name_plural = "Medical Codes"

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

    def __str__(self):
        return '{} {}'.format(self.child, self.medical_codes)
