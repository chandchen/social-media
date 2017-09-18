from django.contrib.auth.models import User
from django.db.models import Q
from django.utils import timezone

from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView

from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    RetrieveUpdateAPIView,
    RetrieveUpdateDestroyAPIView,
    GenericAPIView,
    ListCreateAPIView,
)
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)

from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.response import Response

from upload_app.models import AlbumModel, ImageModel

from .serializers import (
    AlbumListSerializer,
    AlbumDetailSerializer,
    MediaListSerializer,
    MediaCreateSerializer,
    AlbumSerializer,
    AlbumUploadSerializer,
    ImageSerializer,
)

from users.api.pagination import AlbumPagination


class AlbumListCreateAPIView(ListCreateAPIView):
    filter_backends = [SearchFilter, OrderingFilter]
    serializer_class = AlbumListSerializer
    queryset = AlbumModel.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    search_fields = ['title', 'description']
    pagination_class = AlbumPagination

    def get_queryset(self, *args, **kwargs):
        user = self.request.user
        return self.queryset.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class AlbumDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = AlbumDetailSerializer
    queryset = AlbumModel.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self, *args, **kwargs):
        return self.queryset.filter(id=self.kwargs.get('pk'))


class AlbumUploadAPIView(CreateAPIView):
    serializer_class = AlbumUploadSerializer
    queryset = ImageModel.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user,
                        pub_date=timezone.now(),
                        album_id=self.request.GET.get('pk'),)

    # def list(self, request, *args, **kwargs):
    #     queryset = Media.objects.all()
    #     serializer = MediaCreateSerializer(queryset, many=True)
    #     return Response(serializer.data)

    # def create(self, serializer, *args, **kwargs):
    #     queryset = Media.objects.all()
    #     serializer = MediaCreateSerializer(queryset, many=True)
    #     serializer.save(user=self.request.user, date_posted=timezone.now())
#
#
# class MediaListAPIView(ListAPIView):
#     serializer_class = MediaListSerializer
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     search_fields = ['name']
#     pagination_class = AlbumPageNumberPagination
#     filter_backends = [SearchFilter, OrderingFilter]
#
#     def get_queryset(self, *args, **kwargs):
#         user = self.request.user
#         queryset_list = Media.objects.all()
#
#         return queryset_list.filter(user=user, status=0)
#
#
# class ImageListAPIView(ListAPIView):
#     serializer_class = MediaListSerializer
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     search_fields = ['name']
#     pagination_class = AlbumPageNumberPagination
#     filter_backends = [SearchFilter, OrderingFilter]
#
#     def get_queryset(self, *args, **kwargs):
#         user = self.request.user
#         queryset_list = Media.objects.all()
#
#         return queryset_list.filter(user=user, status=0, category=0)
#
#
# class VideoListAPIView(ListAPIView):
#     serializer_class = MediaListSerializer
#     permission_classes = [IsAuthenticatedOrReadOnly]
#
#     def get_queryset(self, *args, **kwargs):
#         user = self.request.user
#         queryset_list = Media.objects.all()
#
#         return queryset_list.filter(user=user, status=0, category=1)
#
#
# class TrashListAPIView(ListAPIView):
#     serializer_class = MediaListSerializer
#     permission_classes = [IsAuthenticatedOrReadOnly]
#
#     def get_queryset(self, *args, **kwargs):
#         user = self.request.user
#         queryset_list = Media.objects.all()
#
#         return queryset_list.filter(user=user, status=1)
#
#
# class MediaCreateAPIView(CreateAPIView):
#     serializer_class = MediaCreateSerializer
#     permission_classes = [IsAuthenticatedOrReadOnly]
#
#     def get_queryset(self, *args, **kwargs):
#         user = self.request.user
#         queryset_list = Album.objects.all()
#
#         return queryset_list.filter(user=user, status=0)
#
#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user, date_posted=timezone.now())
