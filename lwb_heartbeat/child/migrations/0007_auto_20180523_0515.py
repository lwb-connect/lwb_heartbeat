# Generated by Django 2.0.5 on 2018-05-23 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('child', '0006_auto_20180523_0045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='child',
            name='location_country',
            field=models.ForeignKey(on_delete='CASCADE', to='child.Country'),
        ),
    ]