from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib import admin
from django.template import add_to_builtins
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)

urlpatterns += patterns('',
    (r'^feeds/', include('feeds.urls')),
    (r'^notepad/', include('dashboards.urls')),
    (r'^users/', include('users.urls')),
)

urlpatterns += patterns('users.views',
    (r'^accounts/register/$', 'view_register', {'registration_template': 'register.html'}, 'register'),
    (r'^accounts/login/$', 'view_login', {'login_template': 'login.html'}, 'login'),
    (r'^accounts/logout/$', 'view_logout', {'logout_template': 'logout.html'}, 'logout')
)

urlpatterns += patterns('feeds.views',
    (r'^$', 'view_homepage', {'homepage_template':'homepage.html'}, 'homepage'),
)

add_to_builtins("utils.templatetags.tags")