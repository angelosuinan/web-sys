# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-09-27 09:00
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dispersal', '0005_auto_20170927_1654'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='customer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='customer', to='dispersal.Customer'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='invoice',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employee', to=settings.AUTH_USER_MODEL),
        ),
    ]
