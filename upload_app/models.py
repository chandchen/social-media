# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class AlbumModel(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    pub_date = models.DateTimeField('published_date', null=True, blank=True)

    def __unicode__(self):
        return self.user.username


class ImageModel(models.Model):
    user = models.ForeignKey(User)
    album = models.ForeignKey(AlbumModel)
    image = models.ImageField(upload_to="upload_file/images/", null=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    pub_date = models.DateTimeField('published_date', null=True, blank=True)
    status = models.PositiveSmallIntegerField(default=1)

    def __unicode__(self):
        return self.user.username


class FileModel(models.Model):
    user = models.ForeignKey(User)
    # album = models.ForeignKey(AlbumModel)
    file = models.FileField(upload_to="upload_file/file/", null=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    pub_date = models.DateTimeField('published_date', null=True, blank=True)

    def __unicode__(self):
        return self.user.username
