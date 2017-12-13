# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-10-15 12:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dispersal', '0002_customer_organization'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='invoice_number',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Organization')], default='M', max_length=2, verbose_name='Sex'),
        ),
    ]