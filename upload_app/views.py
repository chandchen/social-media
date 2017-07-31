# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render
from .forms import FileUploadForm
from .models import FileSimpleModel, ImageModel


def upload_file(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file_model = FileSimpleModel()
            file_model.file_field = form.cleaned_data['my_file']
            file_model.save()
        return HttpResponse('Upload Success')
    else:
        form = FileUploadForm()
    return render(request, 'upload_app/upload_tem.html', {'form': form})


def upload_image(request):
    if request.method == 'POST':
        new_img = ImageModel(img=request.FILES.get('img'))
        new_img.save()
        return HttpResponse('Upload Success')
    return render(request, 'upload_app/upload_image.html')


def show_image(request):
    imgs = ImageModel.objects.all()
    content = {'img': imgs, }
    return render(request, 'upload_app/show_image.html', content)
