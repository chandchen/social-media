# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils import timezone
from django.contrib.auth.decorators import login_required

from .forms import FileUploadForm, ImageUploadForm, AlbumCreateForm
from .models import FileModel, ImageModel, AlbumModel
from .tasks import transcode_video_task, generate_thumbnail_task

from django.views.generic import TemplateView, FormView, View
from django.core.urlresolvers import reverse_lazy


@login_required
def upload(request):
    return render(request, 'upload_app/upload.html')


# @login_required
# def add_album(request):
#     user = request.user
#     if request.method == 'POST':
#         form = AlbumCreateForm(request.POST)
#         if form.is_valid():
#             form = form.save(commit=False)
#             form.user = user
#             form.pub_date = timezone.now()
#             form.save()
#             return HttpResponseRedirect('/upload/show_album/')
#     else:
#         form = AlbumCreateForm()
#     return render(request, 'upload_app/add_album.html', {'form': form})


class AddAlbumView(FormView):
    form_class = AlbumCreateForm
    success_url = reverse_lazy('upload:show_album')
    template_name = 'upload_app/add_album.html'

    def post(self, request, *args, **kwargs):
        form = AlbumCreateForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.pub_date = timezone.now()
            form.save()
            return HttpResponseRedirect('/upload/show_album/')


# @login_required
# def show_album(request):
#     user = request.user
#     albums = AlbumModel.objects.filter(user=user)
#     return render(request, 'upload_app/show_album.html', {'albums': albums})


class ShowAlbumView(TemplateView):
    template_name = 'upload_app/show_album.html'

    def get_context_data(self, **kwargs):
        user = self.request.user
        albums = AlbumModel.objects.filter(user=user)
        context = super(ShowAlbumView, self).get_context_data(**kwargs)
        context['albums'] = albums
        return context


# @login_required
# def edit_album(request, album_id):
#     user = request.user
#     album = AlbumModel.objects.get(pk=album_id)
#     if request.method == 'POST':
#         form = AlbumCreateForm(request.POST, instance=album)
#         if form.is_valid():
#             form = form.save(commit=False)
#             form.user = user
#             form.pub_date = timezone.now()
#             form.save()
#             return HttpResponseRedirect('/upload/show_image/' + album_id)
#     else:
#         form = AlbumCreateForm(instance=album)
#     return render(request, 'upload_app/edit_album.html', {'form': form})


class EditAlbumView(View):
    form_class = AlbumCreateForm
    template_name = 'upload_app/edit_album.html'

    def get(self, request, *args, **kwargs):
        album = AlbumModel.objects.get(pk=kwargs.get("album_id"))
        form = self.form_class(instance=album)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        album = AlbumModel.objects.get(pk=kwargs.get("album_id"))
        form = self.form_class(request.POST, instance=album)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.pub_date = timezone.now()
            form.save()
            return HttpResponseRedirect('/upload/show_image/' + kwargs.get("album_id"))
        return render(request, self.template_name, {'form': form})


# @login_required
# def delete_album(request, album_id):
#     album = AlbumModel.objects.get(pk=album_id)
#     album.delete()
#     return HttpResponseRedirect('/upload/show_album/')


class DeleteAlbumView(View):

    def get(self, request, *args, **kwargs):
        AlbumModel.objects.get(pk=kwargs.get("album_id")).delete()
        return HttpResponseRedirect('/upload/show_album/')


# @login_required
# def upload_image(request, album_id):
#     user = request.user
#     username = user.username
#     album = AlbumModel.objects.get(pk=album_id)
#     if request.method == 'POST':
#         form = ImageUploadForm(request.POST, request.FILES)
#         if form.is_valid():
#             form = form.save(commit=False)
#             form.user = user
#             form.album = album
#             form.size = request.FILES['image'].size
#             form.name = request.FILES['image'].name
#             form.pub_date = timezone.now()
#             form.save()
#             return HttpResponseRedirect('/upload/show_image/' + album_id)
#     else:
#         form = ImageUploadForm()
#     return render(request, 'upload_app/upload_image.html', {'form': form, 'username': username})


class UploadImageView(View):
    form_class = ImageUploadForm
    template_name = 'upload_app/upload_image.html'

    def get(self, request, *args, **kwargs):
        album = AlbumModel.objects.get(pk=kwargs.get("album_id"))
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        user = request.user
        username = user.username
        album = AlbumModel.objects.get(pk=kwargs.get("album_id"))
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = user
            form.album = album
            form.size = request.FILES['image'].size
            form.name = request.FILES['image'].name
            form.pub_date = timezone.now()
            form.save()
            return HttpResponseRedirect('/upload/show_image/' + kwargs.get("album_id"))
        return render(request, self.template_name, {'form': form, 'username': username})


# @login_required
# def show_image(request, album_id):
#     user = request.user
#     username = user.username
#     album = AlbumModel.objects.get(pk=album_id)
#     images = ImageModel.objects.filter(user=user, album=album, status=1)
#     content = {'images': images, 'username': username, 'album': album}
#     return render(request, 'upload_app/show_image.html', content)


class ShowImageView(TemplateView):
    template_name = 'upload_app/show_image.html'

    def get_context_data(self, **kwargs):
        user = self.request.user
        username = user.username
        album = AlbumModel.objects.get(pk=kwargs.get("album_id"))
        images = ImageModel.objects.filter(user=user, album=album, status=1)
        context = super(ShowImageView, self).get_context_data(**kwargs)
        context['images'] = images
        context['username'] = username
        context['album'] = album
        return context


# @login_required
# def show_image_all(request):
#     user = request.user
#     username = user.username
#     images = ImageModel.objects.filter(user=user, status=1)
#     files = FileModel.objects.filter(user=user)
#     return render(request, 'upload_app/show_image_all.html', {'username': username,
#                                                               'images': images,
#                                                               'files': files, })


class ShowImageAllView(TemplateView):
    template_name = 'upload_app/show_image_all.html'

    def get_context_data(self, **kwargs):
        user = self.request.user
        username = user.username
        images = ImageModel.objects.filter(user=user, status=1)
        files = FileModel.objects.filter(user=user)
        context = super(ShowImageAllView, self).get_context_data(**kwargs)
        context['username'] = username
        context['images'] = images
        context['files'] = files
        return context


@login_required
def show_image_all_by_name(request):
    user = request.user
    username = user.username
    images = ImageModel.objects.filter(user=user, status=1).order_by('description')
    return render(request, 'upload_app/show_image_all.html', {'username': username,
                                                              'images': images, })


@login_required
def show_image_all_by_time(request):
    user = request.user
    username = user.username
    images = ImageModel.objects.filter(user=user, status=1).order_by('pub_date')
    return render(request, 'upload_app/show_image_all.html', {'username': username,
                                                              'images': images, })


@login_required
def show_image_all_by_size(request):
    user = request.user
    username = user.username
    images = ImageModel.objects.filter(user=user, status=1).order_by('size')
    return render(request, 'upload_app/show_image_all.html', {'username': username,
                                                              'images': images, })


@login_required
def image_delete(request, image_id):
    image = ImageModel.objects.get(pk=image_id)
    album_id = str(image.album.id)
    image.delete()
    return HttpResponseRedirect('/upload/trash_detail/')


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
            file_id = FileModel.objects.get(file=form.file).id
            generate_thumbnail_task.delay(file_id)
            transcode_video_task.delay(file_id, hd='640X360')
            transcode_video_task.delay(file_id, hd='hd480')
            transcode_video_task.delay(file_id, hd='hd720')
            return HttpResponseRedirect('/upload/show_file/')
    else:
        form = FileUploadForm()
    return render(request, 'upload_app/upload_file.html', {'form': form, 'username': username})


# @login_required
# def show_file(request):
#     user = request.user
#     username = user.username
#     files = FileModel.objects.filter(user=user)
#     content = {'files': files, 'username': username}
#     return render(request, 'upload_app/show_file.html', content)


class ShowFileView(TemplateView):
    template_name = 'upload_app/show_file.html'

    def get_context_data(self, **kwargs):
        user = self.request.user
        username = user.username
        files = FileModel.objects.filter(user=user)
        context = super(ShowFileView, self).get_context_data(**kwargs)
        context['username'] = username
        context['files'] = files
        return context


@login_required
def show_file_list(request):
    user = request.user
    username = user.username
    files = FileModel.objects.filter(user=user)
    content = {'files': files, 'username': username}
    return render(request, 'upload_app/show_file_list.html', content)


@login_required
def show_file_detail(request, file_id):
    user = request.user
    username = user.username
    file = FileModel.objects.get(pk=file_id)
    content = {'file': file, 'username': username}
    return render(request, 'upload_app/show_file_detail.html', content)


@login_required
def file_delete(request, file_id):
    file = FileModel.objects.get(pk=file_id)
    file.delete()
    return HttpResponseRedirect('/upload/show_file/')


@login_required
def image_trash(request, image_id):
    image = ImageModel.objects.get(pk=image_id)
    album_id = str(image.album.id)
    image.status = 0
    image.save()
    return HttpResponseRedirect('/upload/show_image/' + album_id)


@login_required
def trash_detail(request):
    images = ImageModel.objects.filter(status=0)
    return render(request, 'upload_app/trash_detail.html', {'images': images})


@login_required
def image_restore(request, image_id):
    image = ImageModel.objects.get(pk=image_id)
    image.status = 1
    image.save()
    return HttpResponseRedirect('/upload/trash_detail')
