# Generated by Django 2.0.5 on 2018-05-23 00:45

from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('child', '0005_auto_20180523_0024'),
    ]

    operations = [
        migrations.CreateModel(
            name='LWBProgram',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lwbprogram', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('ED', 'Education'), ('FC', 'Foster Care'), ('MD', 'Medical'), ('TF', 'Traffic Rescue')], max_length=240, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='program',
            name='child',
        ),
        migrations.RenameField(
            model_name='medicalcodes',
            old_name='program',
            new_name='medical_codes',
        ),
        migrations.RemoveField(
            model_name='child',
            name='medical_code',
        ),
        migrations.RemoveField(
            model_name='country',
            name='program',
        ),
        migrations.AddField(
            model_name='medicalcodes',
            name='child',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='medical_codes', to='child.Child'),
        ),
        migrations.DeleteModel(
            name='Program',
        ),
        migrations.AddField(
            model_name='lwbprogram',
            name='child',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lwbprogram', to='child.Child'),
        ),
        migrations.AddField(
            model_name='country',
            name='lwbprogram',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='child.LWBProgram'),
        ),
    ]