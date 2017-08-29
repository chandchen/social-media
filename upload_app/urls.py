from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from . import views


urlpatterns = [
    url(r'^$', views.upload),
    url(r'^upload_file', views.upload_file, name='upload_file'),
    url(r'^upload_image/(?P<album_id>[0-9]+)/$', views.upload_image, name='upload_image'),
    url(r'^show_image/(?P<album_id>[0-9]+)/$', views.show_image, name='show_image'),
    url(r'^show_image/all/$', views.show_image_all, name='show_image_all'),

    url(r'^show_image/all/name$', views.show_image_all_by_name, name='show_image_all_by_name'),
    url(r'^show_image/all/time$', views.show_image_all_by_time, name='show_image_all_by_time'),
    url(r'^show_image/all/size$', views.show_image_all_by_size, name='show_image_all_by_size'),

    url(r'^show_file/$', views.show_file, name='show_file'),
    url(r'^show_file_list/$', views.show_file_list, name='show_file_list'),
    url(r'^show_file_detail/(?P<file_id>[0-9]+)/$', views.show_file_detail, name='show_file_detail'),

    url(r'^image_delete/(?P<image_id>[0-9]+)/$', views.image_delete, name='image_delete'),
    url(r'^image_trash/(?P<image_id>[0-9]+)/$', views.image_trash, name='image_trash'),
    url(r'^image_restore/(?P<image_id>[0-9]+)/$', views.image_restore, name='image_restore'),
    url(r'^trash_detail/$', views.trash_detail, name='trash_detail'),
    url(r'^file_delete/(?P<file_id>[0-9]+)/$', views.file_delete, name='file_delete'),
    url(r'^add_album/$', views.add_album, name='add_album'),
    url(r'^show_album/$', views.show_album, name='show_album'),
    url(r'^delete_album/(?P<album_id>[0-9]+)/$', views.delete_album, name='delete_album'),
    url(r'^edit_album/(?P<album_id>[0-9]+)/$', views.edit_album, name='edit_album'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
