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
    name = models.CharField(max_length=255, default='')
    size = models.PositiveIntegerField(default=0)
    description = models.CharField(max_length=200, null=True, blank=True)
    pub_date = models.DateTimeField('published_date', null=True, blank=True)
    status = models.PositiveSmallIntegerField(default=1)

    def __unicode__(self):
        return self.name


class FileModel(models.Model):
    user = models.ForeignKey(User)
    file = models.FileField(upload_to="upload_file/file/", null=True)
    mp4_360 = models.FileField(upload_to="upload_file/file/mp4_360", blank=True, null=True)
    mp4_480 = models.FileField(upload_to="upload_file/file/mp4_480", blank=True, null=True)
    mp4_720 = models.FileField(upload_to="upload_file/file/mp4_720", blank=True, null=True)
    thumbnail = models.ImageField(upload_to="upload_file/file/thumbnail", blank=True, null=True, default=' ')

    description = models.CharField(max_length=200, null=True, blank=True)
    pub_date = models.DateTimeField('published_date', null=True, blank=True)

    def __unicode__(self):
        return self.user.username
