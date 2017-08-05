# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import FileModel, ImageModel

admin.site.register(FileModel)
admin.site.register(ImageModel)
