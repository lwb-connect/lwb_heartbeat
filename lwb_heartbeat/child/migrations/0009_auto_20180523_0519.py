# Generated by Django 2.0.5 on 2018-05-23 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('child', '0008_auto_20180523_0518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='country_name',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
