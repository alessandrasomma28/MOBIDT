# Generated by Django 4.1.13 on 2024-09-25 14:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('udtApp', '0006_device_metadata_location_trafficflow'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Entity',
        ),
        migrations.AlterModelTable(
            name='device',
            table='entities',
        ),
    ]
