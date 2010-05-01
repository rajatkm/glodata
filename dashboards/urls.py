from django.conf.urls.defaults import *

urlpatterns = patterns('dashboards.views',
    (r'^$', 'view_dashboards', {'dashboards_homepage_template':'dashboards_homepage.html'}, 'notepad'),
    (r'^feeds/all/$', 'view_all_feeds', {'all_feedspage_template':'all_feedspage.html'}, 'all_feed_sources'),        
    (r'^feeds/(?P<feed_id>\d+)/$', 'view_feed_entries_per_feed', {'feedentries_per_feedpage_template':'feed_entries_by_feed_page.html'}, 'feedentries_per_feedpage'),
    (r'^mystuff/$', 'view_user_feedentries', {'user_feedsentries_template':'user_feedentries_page.html'}, 'user_feedentries'),    
)