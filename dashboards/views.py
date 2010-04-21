from utils import response
from feeds.models import Feed, Feedentry
import urllib

def view_dashboards(request, dashboards_homepage_template):
    return response(request, dashboards_homepage_template, {})

def view_all_feeds(request, all_feedspage_template):
    return response(request, all_feedspage_template, {'all_feeds': Feed.objects.all()})

#def view_feed_entries_per_feed(request, feedentries_per_feedpage_template):
#    feedentries_per_feed = Feedentry.objects.filter(feed = "Acme Publishing")
#    return response(request, feedentries_per_feedpage_template, 
#                    {'feedentries_per_feed': Feedentry.objects.get()})