# Generated by Django 2.0.5 on 2018-05-23 18:56

from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('staff', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Child',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('program_number', models.CharField(blank=True, default='CSB000001', max_length=9, null=True, unique=True)),
                ('nick_name', models.CharField(default='Untitled', max_length=180)),
                ('given_name', models.CharField(default='Untitled', max_length=180)),
                ('DOB', models.DateField(blank=True, null=True)),
                ('date_modified', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_name', models.CharField(max_length=30, unique=True)),
                ('children', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='child.Child')),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school', multiselectfield.db.fields.MultiSelectField(choices=[('ED_CAM_BIM_RANGSEI_VILLAGE', 'ED Cambodia Rangsei Village BIM'), ('ED_CAM_BIM_SOKHEM_VILLAGE', 'ED Cambodia Sokhem Village BIM'), ('ED_CAM_BIM_ARY_VILLAGE', 'ED Cambodia Ary Village BIM'), ('ED_CAM_SIB_SOKHEM_VILLAGE', 'ED Cambodia Sokhem Village Sibling School')], max_length=101)),
            ],
        ),
        migrations.CreateModel(
            name='FosterCare',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school', multiselectfield.db.fields.MultiSelectField(choices=[('N/A', 'Not Currently Available'), ('N/A', 'Not Currently Available')], max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='GeneralUpdate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateField(auto_now=True)),
                ('note', models.CharField(default='enter child notes here', max_length=10000)),
                ('child', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='child.Child')),
            ],
        ),
        migrations.CreateModel(
            name='GrowthData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_recorded', models.DateField(auto_now=True)),
                ('height', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('weight', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('concern_flag', models.BooleanField(default=False)),
                ('child', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='child.Child')),
            ],
        ),
        migrations.CreateModel(
            name='HealingHome',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school', multiselectfield.db.fields.MultiSelectField(choices=[('N/A', 'Not Currently Available')], max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='LWBProgram',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lwbprogram', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('ED', 'Education'), ('FC', 'Foster Care'), ('MD', 'Medical'), ('TF', 'Traffic Rescue')], max_length=240, null=True)),
                ('child', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lwbprogram', to='child.Child')),
            ],
        ),
        migrations.CreateModel(
            name='Medical',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school', multiselectfield.db.fields.MultiSelectField(choices=[('N/A', 'Not Currently Available')], max_length=3)),
                ('medical_program', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='medical_program', to='child.LWBProgram')),
            ],
        ),
        migrations.CreateModel(
            name='MedicalCodes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medical_codes', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('AA', 'AA Anal Atresia'), ('AB', 'AB Amniotonic Banding'), ('AN', 'AN Animal Injury'), ('AU', 'AU Auditory Issues'), ('BA', 'BA Biliary Atresia'), ('BE', 'BE Bladder Extrophy'), ('BI', 'BI Burn Injury'), ('BL', 'BL Blood Issues'), ('CA', 'CA Cancer'), ('CF', 'CF Club Feet'), ('CH', 'CH Club Hands'), ('CJ', 'CJ Conjoined Twins'), ('CL', 'CL Cleft Lip'), ('CP', 'CP Cleft Palate'), ('EA', 'EA Esophageal Atresia'), ('EV', 'EV Evaluation'), ('EY', 'EY Eye Issues'), ('FT', 'FT Failure to Thrive'), ('GE', 'GE Genital Issues'), ('GI', 'GI Gastrointestinal'), ('GS', 'GS General Sergery'), ('HE', 'HE Hernia Surgery'), ('HM', 'HM Hemangioma Surgery'), ('HT', 'HT Heart Surgery'), ('IF', 'IF Infection Treatment'), ('IJ', 'IJ Injury'), ('MT', 'MT Medical Testing'), ('NE', 'NE Neurologic Issues'), ('OR', 'OR Orthopedic Issues'), ('PN', 'PN Pneumonia Treatment'), ('PR', 'PR Premature Newbord Care'), ('PT', 'PT Physical Therapy'), ('PU', 'PU Pulmonary Issues'), ('RI', 'RI Renal Issues'), ('TU', 'TU Tumors (ex. Teratomas'), ('UR', 'UR Urologic Issues')], max_length=240, null=True)),
                ('child', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='medical_codes', to='child.Child')),
            ],
        ),
        migrations.CreateModel(
            name='MedicalUpdate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateField(auto_now=True)),
                ('date_edited', models.DateField()),
                ('medical_note', models.CharField(blank=True, default='enter child notes here', max_length=10000, null=True)),
                ('child', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='child.Child')),
            ],
        ),
        migrations.CreateModel(
            name='Nutrition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school', multiselectfield.db.fields.MultiSelectField(choices=[('N/A', 'Not Currently Available')], max_length=3)),
                ('nutrition_program', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='nutrition_program', to='child.LWBProgram')),
            ],
        ),
        migrations.CreateModel(
            name='Trafficking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school', multiselectfield.db.fields.MultiSelectField(choices=[('N/A', 'Not Currently Available')], max_length=3)),
                ('trafficking_program', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='trafficking_program', to='child.LWBProgram')),
            ],
        ),
        migrations.AddField(
            model_name='healinghome',
            name='healing_home_program',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='healing_home', to='child.LWBProgram'),
        ),
        migrations.AddField(
            model_name='fostercare',
            name='foster_program',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='foster_care', to='child.LWBProgram'),
        ),
        migrations.AddField(
            model_name='education',
            name='education_program',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='education_program', to='child.LWBProgram'),
        ),
        migrations.AddField(
            model_name='country',
            name='lwbprogram',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='child.LWBProgram'),
        ),
        migrations.AddField(
            model_name='country',
            name='staff',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='staff.StaffProfile'),
        ),
        migrations.AddField(
            model_name='child',
            name='location_country',
            field=models.ForeignKey(on_delete='CASCADE', to='child.Country'),
        ),
    ]
