# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-09-30 13:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_item_photo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='recieved_by',
            new_name='received_by',
        ),
    ]
