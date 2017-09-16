from django.conf.urls import url

from .views import UserCreateAPIView, UserProfileAPIView, UserListAPIView, UserDetailAPIView


urlpatterns = [
    url(r'^$', UserListAPIView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)', UserDetailAPIView.as_view(), name='detail'),
    url(r'^register/$', UserCreateAPIView.as_view(), name='register'),
    url(r'^profile/(?P<pk>[\d-]+)/$', UserProfileAPIView.as_view(), name='profile'),
]
