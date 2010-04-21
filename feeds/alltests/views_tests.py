from utils import TestCase
from django.core.urlresolvers import reverse as url_reverse
from feeds.models import Feed, FeedEntry

class SearchPage_Tests(TestCase):
    fixtures = ['feeds.json', 'feedentries.json']

    def test_searchpage_url(self):
        response = self.client.get(url_reverse('feeds.views.view_search'))
        self.assertTrue(response)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'search.html')
        context = response.context[0]
        self.assertTrue(context.has_key('feedentries'))
        feedentries = context.get('feedentries')
        self.assertFalse(feedentries)
        self.assertTrue(context.has_key('form'))
        
    def test_searchpage_with_invalid_query(self):
        response = self.client.post(url_reverse('feeds.views.view_search'), data={'query':''})
        self.assertTrue(response)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'search.html')
        context = response.context[0]
        self.assertTrue(context.has_key('form'))
        form = context.get('form')
        self.assertTrue(form.errors)
        self.assertTrue(form.errors.get('query'))
    
    def test_searchpage_with_valid_query(self):
        response = self.client.post(url_reverse('feeds.views.view_search'), data={'query':'google'})
        self.assertTrue(response)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'search.html')
        context = response.context[0]
        self.assertTrue(context.has_key('form'))
        self.assertTrue(context.has_key('feedentries'))
        feedentries = context.get('feedentries')
        self.assertTrue(feedentries)
        
class FeedPage_Tests(TestCase):
    fixtures = ['feeds.json', 'feedentries.json']

    def test_feedpage_url(self):
        latest_feed = Feed.objects.latest()
        response = self.client.get(url_reverse('feeds.views.view_feed_profile', args=(latest_feed.id,)))
        self.assertTrue(response)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'feed_profile.html')
        context = response.context[0]
        self.assertTrue(context.has_key('feed'))
        feed = context.get('feed')
        self.assertEquals(feed.id, latest_feed.id)
        self.assertTrue(feed)
        self.assertFalse(feed.blocked)
        self.assertTrue(feed.feedentries)
        
    def test_invalid_feedpage_url(self):
        response = self.client.get(url_reverse('feeds.views.view_feed_profile', args=(1234,)))
        self.assertTrue(response)
        self.assertEquals(response.status_code, 404)
        
class FeedEntryPage_Tests(TestCase):
    fixtures = ['feeds.json', 'feedentries.json']

    def test_feedentrypage_url(self):
        latest_feedentry = FeedEntry.objects.latest()
        response = self.client.get(url_reverse('feeds.views.view_feedentry_profile', args=(latest_feedentry.id,latest_feedentry.slug)))
        self.assertTrue(response)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'feedentry_profile.html')
        context = response.context[0]
        self.assertTrue(context.has_key('feedentry'))
        feedentry = context.get('feedentry')
        self.assertEquals(feedentry.id, latest_feedentry.id)
        self.assertTrue(feedentry)
        
    def test_invalid_feedpage_url(self):
        response = self.client.get(url_reverse('feeds.views.view_feedentry_profile', args=(1234,'zyz')))
        self.assertTrue(response)
        self.assertEquals(response.status_code, 404)