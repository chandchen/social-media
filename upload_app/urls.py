from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from . import views


urlpatterns = [
    url(r'^$', views.upload),
    url(r'^upload_file', views.upload_file, name='upload_file'),
    url(r'^upload_image/$', views.upload_image, name='upload_image'),
    url(r'^show_image/$', views.show_image, name='show_image'),
    url(r'^show_file/$', views.show_file, name='show_file'),
    url(r'^image_delete/(?P<image_id>[0-9]+)/$', views.image_delete, name='image_delete'),
    url(r'^file_delete/(?P<file_id>[0-9]+)/$', views.file_delete, name='file_delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
