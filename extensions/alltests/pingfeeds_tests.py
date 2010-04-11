from utils import TestCase

class PingFeedsExtension_Tests(TestCase):
#    fixtures = ['PingFeeds.json']

    def test_pingfeeds_with_valid_rss_url(self):
        from feedbox.models import FeedEntry
        self.assertFalse(FeedEntry.objects.count())
        from feedbox.models import Feed
        feed = Feed.objects.create_feed(url='http://feeds.feedburner.com/blogspot/MKuf', name='Official Google Blog')
        #TODO:Feed creation should go in a fixture. Its failing to load
        #fixtures. Need to check why
        from extensions.management.commands import pingfeeds
        pingfeeds.ping_feeds()
        self.assertTrue(FeedEntry.objects.count())
        feedentries = FeedEntry.objects.all()
        for feedentry in feedentries:
            self.assertEquals(feedentry.feed, feed)
        from datetime import datetime, timedelta
        feed_latest_updated_time = Feed.objects.get(url=feed.url).last_updated
        self.assertTrue(feed_latest_updated_time > (datetime.now()-timedelta(minutes=1)) and feed_latest_updated_time < datetime.now())
        
        
