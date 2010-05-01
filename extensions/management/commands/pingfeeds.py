from datetime import datetime
from django.core.management.base import NoArgsCommand
from feeds.models import FeedEntry, Feed
from libs.feedparser import parse as parse_feed

class Command(NoArgsCommand):
    help = "Pings all the feeds and creates feedentries"

    def handle_noargs(self, **options):
        return ping_feeds()
        
def ping_feeds():
    print 'Going to ping %s feeds...' % Feed.objects.count()
    for feed in Feed.objects.all():
        ping_feed(feed)
    print 'Ping Complete.'
    
def ping_feed(feed):
    print 'Pinging %s feed...' % feed.name
    feed_response = parse_feed(feed.url)
    try:
        _process_feed_response(feed_response, feed)
    except Exception, e:
        print 'Error while processing the feed response for feed:%s\nMessage:%s' % (feed, e.__str__())

def _process_feed_response(feed_response, feed):
    entries = feed_response['entries']
    for entry in entries:
        try:
            FeedEntry.objects.create_feedentry(title=entry.title,
                                               desc=entry.description,
                                               url=entry.link,
                                               feed=feed)
        except Exception,e:
            print 'Error in creating the feedentry:%s\nMessage:%s' % (entry.title, e.__str__()) 
    feed.last_updated = datetime.now()
    feed.save()