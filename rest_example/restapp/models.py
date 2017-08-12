# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models



# Create your models here.
class Post(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    content = models.TextField()

    class Meta:
        ordering = ('created',)


class Events(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    content = models.TextField()
    data_id = models.IntegerField(default=123)


class Client(models.Model):
    name = models.CharField(max_length=30) 
    contactEmail = models.EmailField(max_length=30)
    contactPhone = models.CharField(max_length=30)
    contactPerson = models.CharField(max_length=30)

    class Meta:
        db_table = 'contact_info'