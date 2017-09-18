from django.contrib.auth.models import User

from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField,
    SerializerMethodField,
    StringRelatedField,
    PrimaryKeyRelatedField,
)
from rest_framework import serializers

from upload_app.models import AlbumModel, ImageModel, FileModel


album_detail_url = HyperlinkedIdentityField(
    view_name='upload-api:album-detail'
)
# album_update_url = HyperlinkedIdentityField(
#     view_name='upload-api:album-update'
# )
# album_delete_url = HyperlinkedIdentityField(
#     view_name='upload-api:album-delete'
# )
# album_upload_url = HyperlinkedIdentityField(
#     view_name='upload-api:album-upload'
# )


class AlbumListSerializer(ModelSerializer):
    detail = album_detail_url

    class Meta:
        model = AlbumModel
        fields = [
            'user',
            'title',
            'description',
            'pub_date',
            'detail',
        ]
        read_only_fields = [
            'user',
        ]


class ImageSerializer(ModelSerializer):

    class Meta:
        model = ImageModel
        fields = [
            'album',
            'image',
            'name',
            'size',
            'description',
            'pub_date',
            'status',
        ]


class AlbumDetailSerializer(ModelSerializer):
    images = ImageSerializer(many=True)

    class Meta:
        model = AlbumModel
        fields = [
            'title',
            'description',
            'pub_date',
            'images',
        ]
        read_only_fields = [
            'user',
        ]


class AlbumUploadSerializer(ModelSerializer):

    class Meta:
        model = ImageModel
        fields = [
            'image',
            'description',
        ]


class MediaListSerializer(ModelSerializer):

    class Meta:
        model = ImageModel
        fields = '__all__'


class MediaSerializer(ModelSerializer):

    class Meta:
        model = ImageModel
        fields = [
            'media',
        ]


class AlbumSerializer(ModelSerializer):
    media = MediaSerializer()

    class Meta:
        model = AlbumModel
        fields = [
            'title',
            'media'
        ]

    def create(self, validated_data):
        media_data = validated_data.pop('media')
        album = AlbumModel.objects.get(validated_data.get('title'))
        ImageModel.objects.create(album=album, **media_data)
        return album


class MediaCreateSerializer(ModelSerializer):
    # album = GetUserAlbumSerializer(source='user.username')
    # album = SerializerMethodField()

    class Meta:
        model = ImageModel
        fields = [
            'album',
            'name',
            'media',
        ]

    # def create(self, validated_data):
    #     return Media(**validated_data)

    # def get_album(self, obj):
    #     return obj.album.filter(user=10)
