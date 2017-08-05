# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils import timezone
from django.contrib.auth.decorators import login_required

from .forms import FileUploadForm, ImageUploadForm
from .models import FileModel, ImageModel


@login_required
def upload(request):
    return render(request, 'upload_app/upload.html')


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
def upload_image(request):
    user = request.user
    username = user.username
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = user
            form.pub_date = timezone.now()
            form.save()
        return HttpResponseRedirect('/upload/show_image/')
    else:
        form = ImageUploadForm()
    return render(request, 'upload_app/upload_image.html', {'form': form, 'username': username})


@login_required
def show_image(request):
    user = request.user
    username = user.username
    images = ImageModel.objects.filter(user=user)
    content = {'images': images, 'username': username}
    return render(request, 'upload_app/show_image.html', content)


@login_required
def show_file(request):
    user = request.user
    username = user.username
    files = FileModel.objects.all()
    content = {'files': files, 'username': username}
    return render(request, 'upload_app/show_file.html', content)


@login_required
def image_delete(request, image_id):
    image = ImageModel.objects.get(pk=image_id)
    image.delete()
    return HttpResponseRedirect('/upload/show_image/')


@login_required
def file_delete(request, file_id):
    file = FileModel.objects.get(pk=file_id)
    file.delete()
    return HttpResponseRedirect('/upload/show_file/')
