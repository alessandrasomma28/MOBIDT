# Generated by Django 5.1.1 on 2024-09-25 13:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('udtApp', '0005_entity'),
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('_id', models.JSONField(primary_key=True, serialize=False)),
                ('attrNames', models.JSONField()),
                ('attrs', models.JSONField()),
                ('creDate', models.FloatField()),
                ('modDate', models.FloatField()),
                ('lastCorrelator', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Metadata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('observedAt', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.JSONField()),
                ('type', models.CharField(max_length=50)),
                ('creDate', models.FloatField()),
                ('modDate', models.FloatField()),
                ('md', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='udtApp.metadata')),
            ],
        ),
        migrations.CreateModel(
            name='TrafficFlow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField()),
                ('type', models.CharField(max_length=50)),
                ('creDate', models.FloatField()),
                ('modDate', models.FloatField()),
                ('md', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='udtApp.metadata')),
            ],
        ),
    ]
