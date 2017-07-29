from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic.base import TemplateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='users/index.html'), name='index'),
    url(r'^users/', include('users.urls', namespace='users')),
]
