# Generated by Django 5.1.6 on 2025-03-03 07:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('optimizer', '0007_remove_distributionrecord_supply_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='distributionrecord',
            name='supply',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='optimizer.medicalsupply'),
        ),
    ]
