# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-10-15 16:53
from __future__ import unicode_literals

from django.db import migrations, models
import inventory.models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0008_item_property_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='property_number',
            field=models.CharField(blank=True, default=inventory.models.increment_property_number, max_length=500, null=True),
        ),
    ]
