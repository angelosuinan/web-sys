# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-10-02 06:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dispersal', '0008_auto_20170927_1912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='free',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
