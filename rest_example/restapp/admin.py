# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Post,Events,Client

admin.site.register(Events)
admin.site.register(Post)
admin.site.register(Client)