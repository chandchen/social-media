from django import forms

from .models import FileModel, ImageModel, AlbumModel


class AlbumCreateForm(forms.ModelForm):

    class Meta:
        model = AlbumModel
        fields = ('title', 'description')


class ImageUploadForm(forms.ModelForm):

    class Meta:
        model = ImageModel
        fields = ('image', 'description')


class FileUploadForm(forms.ModelForm):

    class Meta:
        model = FileModel
        fields = ('file', 'description')
