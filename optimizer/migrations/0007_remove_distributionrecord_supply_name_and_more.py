# Generated by Django 5.1.6 on 2025-03-03 07:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('optimizer', '0006_alter_hospital_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='distributionrecord',
            name='supply_name',
        ),
        migrations.AddField(
            model_name='distributionrecord',
            name='supply',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='optimizer.medicalsupply'),
        ),
    ]
