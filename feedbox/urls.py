from django.conf.urls.defaults import *

urlpatterns = patterns('feedbox.views',
    (r'^$', 'view_all_feeds', {'all_feeds_template':'all_feeds_page.html'}, 'all_feeds'),
)