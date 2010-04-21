from django.conf.urls.defaults import *
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)

urlpatterns += patterns('',
    (r'^ScribblePad/', include('dashboards.urls')),
#    (r'^feeds/', include('feeds.urls')),
)

urlpatterns += patterns('feeds.views',
    (r'^$', 'view_homepage', {'homepage_template':'homepage.html'}, 'homepage'),
)