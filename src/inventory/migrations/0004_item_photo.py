# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-09-30 12:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_auto_20170930_2044'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='photo',
            field=models.FileField(blank=True, upload_to='inventory/'),
        ),
    ]
