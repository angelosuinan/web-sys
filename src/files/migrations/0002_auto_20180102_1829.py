# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-01-02 10:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='name',
        ),
        migrations.AlterField(
            model_name='file',
            name='upload',
            field=models.FileField(upload_to='files/'),
        ),
    ]
