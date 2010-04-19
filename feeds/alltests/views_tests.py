from utils import TestCase
from django.core.urlresolvers import reverse as url_reverse

class SearchPage_Tests(TestCase):
    fixtures = ['feeds.json', 'feedentries.json']

    def test_searchpage_url(self):
        response = self.client.get(url_reverse('feeds.views.view_search'))
        self.assertTrue(response)
        self.assertEquals(response.status_code, 200)
        context = response.context[0]
        self.assertTrue(context.has_key('feedentries'))
        feedentries = context.get('feedentries')
        self.assertFalse(feedentries)
        self.assertTrue(context.has_key('form'))
        
    def test_searchpage_with_invalid_query(self):
        response = self.client.post(url_reverse('feeds.views.view_search'), data={'query':''})
        self.assertTrue(response)
        self.assertEquals(response.status_code, 200)
        context = response.context[0]
        self.assertTrue(context.has_key('form'))
        form = context.get('form')
        self.assertTrue(form.errors)
        self.assertTrue(form.errors.get('query'))
    
    def test_searchpage_with_valid_query(self):
        response = self.client.post(url_reverse('feeds.views.view_search'), data={'query':'google'})
        self.assertTrue(response)
        self.assertEquals(response.status_code, 200)
        context = response.context[0]
        self.assertTrue(context.has_key('form'))
        self.assertTrue(context.has_key('feedentries'))
        feedentries = context.get('feedentries')
        self.assertTrue(feedentries)