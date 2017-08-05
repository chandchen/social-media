from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic.base import TemplateView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='users/index.html'), name='index'),
    url(r'^users/', include('users.urls', namespace='users')),
    url(r'^upload/', include('upload_app.urls', namespace='upload')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
