# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-10 18:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restapp', '0002_event'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Event',
            new_name='Events',
        ),
    ]
