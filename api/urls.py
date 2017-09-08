# from django.conf.urls import url, include
# from rest_framework import routers
#
# from . import views
#
# router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet, base_name='user')
# router.register(r'profile', views.ProfileViewSet, base_name='profile')
#
#
# urlpatterns = [
#     url(r'', include(router.urls)),
# ]

from django.conf.urls import url, include

from .views import UserList, UserDetail
from .views import PostList, PostDetail, UserPostList
from .views import PhotoList, PhotoDetail, PostPhotoList

from .views import ProfileList, ProfileDetail, LoginView

user_urls = [
    url(r'^(?P<username>[0-9a-zA-Z_-]+)/posts$', UserPostList.as_view(), name='userpost-list'),
    url(r'^(?P<username>[0-9a-zA-Z_-]+)$', UserDetail.as_view(), name='user-detail'),
    url(r'^$', UserList.as_view(), name='user-list')
]

post_urls = [
    url(r'^(?P<pk>\d+)/photos$', PostPhotoList.as_view(), name='postphoto-list'),
    url(r'^(?P<pk>\d+)$', PostDetail.as_view(), name='post-detail'),
    url(r'^$', PostList.as_view(), name='post-list')
]

photo_urls = [
    url(r'^(?P<pk>\d+)$', PhotoDetail.as_view(), name='photo-detail'),
    url(r'^$', PhotoList.as_view(), name='photo-list')
]

urlpatterns = [
    url(r'^users/', include(user_urls)),
    url(r'^posts/', include(post_urls)),
    url(r'^photos/', include(photo_urls)),
    url(r'^profile/$', ProfileList.as_view(), name='profile-list'),
    url(r'^profile/(?P<pk>\d+)$', ProfileDetail.as_view(), name='profile-detail'),
    url(r'^login/$', LoginView.as_view(), name='login'),
]
