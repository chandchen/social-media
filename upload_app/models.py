# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class FileSimpleModel(models.Model):
    file_field = models.FileField(upload_to="upload_file/")


class ImageModel(models.Model):
    img = models.ImageField(upload_to="upload_file/img")
