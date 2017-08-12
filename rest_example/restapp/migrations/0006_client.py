# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-11 10:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapp', '0005_events_data_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('contactEmail', models.EmailField(max_length=30)),
                ('contactPhone', models.CharField(max_length=30)),
                ('contactPerson', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'contact_info',
            },
        ),
    ]
