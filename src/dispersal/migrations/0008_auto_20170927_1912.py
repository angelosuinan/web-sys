# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-09-27 11:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dispersal', '0007_invoice_total_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='free',
            field=models.IntegerField(blank=True),
        ),
    ]