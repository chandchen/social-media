# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class FileModel(models.Model):
    user = models.ForeignKey(User)
    file = models.FileField(upload_to="upload_file/file/", null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    pub_date = models.DateTimeField('published_date', null=True, blank=True)

    def __unicode__(self):
        return self.user.username


class ImageModel(models.Model):
    user = models.ForeignKey(User)
    image = models.ImageField(upload_to="upload_file/images/", null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    pub_date = models.DateTimeField('published_date', null=True, blank=True)

    def __unicode__(self):
        return self.user.username
