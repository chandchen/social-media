# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Post, Photo


admin.site.register(Post)
admin.site.register(Photo)
