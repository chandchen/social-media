from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views as core_views

urlpatterns = [
    url(r'^register/$', core_views.register, name='register'),
    url(r'^login/$', auth_views.login, {'template_name': 'users/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'users/logout.html'}, name='logout'),
    url(r'^change/$', auth_views.password_change, {'template_name': 'users/change.html',
                                                   'post_change_redirect': 'users:change_done'}, name='change'),
    url(r'^change_done/$', auth_views.password_change_done, {'template_name': 'users/change_done.html'},
        name='change_done'),
]
