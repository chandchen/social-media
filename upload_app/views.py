# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils import timezone
from django.contrib.auth.decorators import login_required

from .forms import FileUploadForm, ImageUploadForm, AlbumCreateForm
from .models import FileModel, ImageModel, AlbumModel


@login_required
def upload(request):
    return render(request, 'upload_app/upload.html')


@login_required
def add_album(request):
    user = request.user
    if request.method == 'POST':
        form = AlbumCreateForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = user
            form.pub_date = timezone.now()
            form.save()
        return HttpResponseRedirect('/upload/show_album/')
    else:
        form = AlbumCreateForm()
    return render(request, 'upload_app/add_album.html', {'form': form})


@login_required
def show_album(request):
    user = request.user
    albums = AlbumModel.objects.filter(user=user)
    return render(request, 'upload_app/show_album.html', {'albums': albums})


@login_required
def edit_album(request, album_id):
    user = request.user
    album = AlbumModel.objects.get(pk=album_id)
    if request.method == 'POST':
        form = AlbumCreateForm(request.POST, instance=album)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = user
            form.pub_date = timezone.now()
            form.save()
        return HttpResponseRedirect('/upload/show_album/')
    else:
        form = AlbumCreateForm(instance=album)
    return render(request, 'upload_app/edit_album.html', {'form': form})


@login_required
def delete_album(request, album_id):
    album = AlbumModel.objects.get(pk=album_id)
    album.delete()
    return HttpResponseRedirect('/upload/show_album/')


@login_required
def upload_image(request, album_id):
    user = request.user
    username = user.username
    album = AlbumModel.objects.get(pk=album_id)
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = user
            form.album = album
            form.pub_date = timezone.now()
            form.save()
        return HttpResponseRedirect('/upload/show_album/')
    else:
        form = ImageUploadForm()
    return render(request, 'upload_app/upload_image.html', {'form': form, 'username': username})


@login_required
def show_image(request, album_id):
    user = request.user
    username = user.username
    album = AlbumModel.objects.get(pk=album_id)
    images = ImageModel.objects.filter(user=user, album=album, status=1)
    content = {'images': images, 'username': username, 'album': album}
    return render(request, 'upload_app/show_image.html', content)


@login_required
def image_delete(request, image_id):
    image = ImageModel.objects.get(pk=image_id)
    image.delete()
    return HttpResponseRedirect('/upload/show_album/')


@login_required
def upload_file(request):
    user = request.user
    username = user.username
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = user
            form.pub_date = timezone.now()
            form.save()
        return HttpResponseRedirect('/upload/show_file/')
    else:
        form = FileUploadForm()
    return render(request, 'upload_app/upload_file.html', {'form': form, 'username': username})


@login_required
def show_file(request):
    user = request.user
    username = user.username
    files = FileModel.objects.filter(user=user)
    content = {'files': files, 'username': username}
    return render(request, 'upload_app/show_file.html', content)


@login_required
def file_delete(request, file_id):
    file = FileModel.objects.get(pk=file_id)
    file.delete()
    return HttpResponseRedirect('/upload/show_file/')


@login_required
def image_trash(request, image_id):
    image = ImageModel.objects.get(pk=image_id)
    image.status = 0
    image.save()
    return HttpResponseRedirect('/upload/show_album')


@login_required
def trash_detail(request):
    images = ImageModel.objects.filter(status=0)
    return render(request, 'upload_app/trash_detail.html', {'images': images})


@login_required
def image_restore(request, image_id):
    image = ImageModel.objects.get(pk=image_id)
    image.status = 1
    image.save()
    return HttpResponseRedirect('/upload/show_album')
