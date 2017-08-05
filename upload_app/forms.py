from django import forms

from .models import FileModel, ImageModel


class FileUploadForm(forms.ModelForm):

    class Meta:
        model = FileModel
        fields = ('file', 'description')


class ImageUploadForm(forms.ModelForm):

    class Meta:
        model = ImageModel
        fields = ('image', 'description')
