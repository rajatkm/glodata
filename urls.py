from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('feeds.views',
    (r'^$', 'view_homepage', {'homepage_template':'homepage.html'}, 'homepage'),
)