from django.core.management.base import NoArgsCommand
from libs.feedparser import parse as parse_feed
from feedbox.models import FeedEntry

class Command(NoArgsCommand):
    help = "Pings all the feeds and creates feedentries"
    
    def handle_noargs(self, **options):
        from feedbox.models import Feed
        print 'Going to ping %s feeds' % Feed.objects.count()
        for feed in Feed.objects.all():
            feed_response = parse_feed(feed.url)
            try:
                self.process_feed_response(feed_response,feed)
            except Exception,e:
                print 'Error while processing the feed response for feed:%s\nMessage:%s' % (feed, e.__str__())
        print 'Ping Complete...'
            
    def process_feed_response(self, feed_response, feed):
        entries = feed_response['entries']
        for entry in entries:
            feedentry = FeedEntry.objects.create_feedentry(title=entry.title,
                                                           desc=entry.summary,
                                                           url=entry.link,
                                                           feed=feed)