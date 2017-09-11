from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^register/$', views.RegisterView.as_view(), name='register'),
    url(r'^login/$', auth_views.login, {'template_name': 'users/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'users/logout.html'}, name='logout'),

    # Change Password
    url(r'^change/$', auth_views.password_change, {'template_name': 'users/change.html',
                                                   'post_change_redirect': 'users:change_done'}, name='change'),
    url(r'^change_done/$', auth_views.password_change_done, {'template_name': 'users/change_done.html'},
        name='change_done'),

    # Reset Password
    url(r'^reset/$', auth_views.password_reset, {'template_name': 'users/registration/reset_form.html',
                                                 'post_reset_redirect': 'users:reset_done'}, name='reset_form'),
    url(r'^reset_done/$', auth_views.password_reset_done, {'template_name': 'users/registration/reset_done.html'},
        name='reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, {'template_name': 'users/registration/reset_confirm.html',
                                            'post_reset_redirect': 'users:reset_complete'}, name='reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete,
        {'template_name': 'users/registration/reset_complete.html'}, name='reset_complete'),

    # User Profile
    url(r'^profile/(?P<pk>\d+)/$', views.ProfileView.as_view(), name='profile_view'),
    url(r'^profile/(?P<pk>\d+)/edit/$', views.ProfileEditView.as_view(), name='profile_edit'),
]
