from utils import response
from feeds.models import Feed, FeedEntry
from dashboards.models import UserFeedEntry
import urllib
from django.shortcuts import get_object_or_404

def view_dashboards(request, dashboards_homepage_template):
    return response(request, dashboards_homepage_template, {})

def view_all_feeds(request, all_feedspage_template):
    return response(request, all_feedspage_template, {'all_feeds': Feed.objects.all()})

def view_feed_entries_per_feed(request, feed_id, feedentries_per_feedpage_template):
    if request.method == 'POST':
        user_feedentries = request.POST.getlist('feedentry')
        for user_feedentry in user_feedentries:
            print user_feedentry.value
            #UserFeedEntry.objects.create_user_feedentry(feedentry=feed)
    else:
        feed = get_object_or_404(Feed, id=int(feed_id))
        return response(request, feedentries_per_feedpage_template, 
                        {'feedentries_per_feed': FeedEntry.objects.filter(feed=feed), 
                         'feed_id': feed_id, 'feed': feed})
    return response(request, search_template, {'form': form,
                                               'feedentries': feedentries})