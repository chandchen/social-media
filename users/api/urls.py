from django.conf.urls import url

from .views import UserCreateAPIView, UserProfileAPIView


urlpatterns = [
    url(r'^register/$', UserCreateAPIView.as_view(), name='register'),
    url(r'^profile/(?P<pk>[\d-]+)/$', UserProfileAPIView.as_view(), name='profile'),
]
