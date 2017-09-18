from rest_framework.pagination import (
    PageNumberPagination,
)


class UsersPagination(PageNumberPagination):
    page_size = 3


class AlbumPagination(PageNumberPagination):
    page_size = 3
