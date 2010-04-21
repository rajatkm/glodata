from django.conf.urls.defaults import *

urlpatterns = patterns('dashboards.views',
    (r'^$', 'view_dashboards', {'dashboards_homepage_template':'dashboards_homepage.html'}, 'ScribblePad'),
    (r'^feeds/all$', 'view_all_feeds', {'all_feedspage_template':'all_feedspage.html'}, 'all_feed_sources'),        
)
