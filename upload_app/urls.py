from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from . import views


urlpatterns = [
    url(r'^$', views.upload_file),
    url(r'^upload_image/$', views.upload_image),
    url(r'^show_image/$', views.show_image),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
