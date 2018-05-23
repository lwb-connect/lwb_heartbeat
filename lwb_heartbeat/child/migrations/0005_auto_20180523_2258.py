# Generated by Django 2.0.5 on 2018-05-23 22:58

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('child', '0004_child_education_program'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lwbprogram',
            name='lwbprogram',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('ED', 'Education'), ('FC', 'Foster Care'), ('MD', 'Medical'), ('TF', 'Safe Haven'), ('NT', 'Nutrition'), ('HH', 'Healing Home')], max_length=240, null=True),
        ),
    ]
