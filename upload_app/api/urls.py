from django.conf.urls import url

from .views import (
    AlbumListCreateAPIView,
    AlbumDetailAPIView,
    AlbumUploadAPIView,
    # MediaListAPIView,
    # ImageListAPIView,
    # VideoListAPIView,
    # TrashListAPIView,
    # MediaCreateAPIView,
    # AlbumUploadAPIView,
)


urlpatterns = [
    url('^album/$', AlbumListCreateAPIView.as_view(), name='album-list'),
    url('^album/(?P<pk>\d+)/$',
        AlbumDetailAPIView.as_view(), name='album-detail'),

    url('^album/(?P<pk>\d+)/upload/$', AlbumUploadAPIView.as_view(),
        name='album-upload'),
#
#     url('^medias/$', MediaListAPIView.as_view(), name='media-list'),
#     url('^images/$', ImageListAPIView.as_view(), name='image-list'),
#     url('^videos/$', VideoListAPIView.as_view(), name='video-list'),
#     url('^trashes/$', TrashListAPIView.as_view(), name='trash-list'),
]
