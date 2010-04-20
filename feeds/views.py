from feeds.models import FeedEntry, Feed
from django.conf import settings
from utils import response, post_data
from xml.dom import minidom
from django.db.models import Q
import urllib
from django.shortcuts import get_object_or_404

def view_all_feeds(request, all_feeds_template):
    return response(request, all_feeds_template, {'all_feeds': Feed.activeobjects.all()})

def view_save_feed(request, all_feeds_template):
    #FIXME:Move this entire view code to a command extension.
    #Views are implicitly assumed to be called by the "browser" 'get' operation 
    for url_obj in Feed.objects.all():
        #FIXME:Feed.objects.all() returns all feed objects.  And not "url_obj"s
        #So change url_obj to feed

        #FIXME:And refactor the below functionality into functions. Like,
        #1)ping feed, 2)process feed response, etc...

        #FIXME:Never, ever use variables like fp, file or something. Have 
        #a context related variable name
        url = url_obj.source_url
        fp = urllib.urlopen(url)
        xmldoc = minidom.parse(fp)
        xmlitem = xmldoc.getElementsByTagName('item')
        #FIXME:xmldoc.getElementsByTagName returns objects(plural). So,
        #rename the 'xmlitem' to 'feeditems' 
        for item in xmlitem:
            title = item.getElementsByTagName('title')[0].firstChild.data
            pub_date = item.getElementsByTagName('pubDate')[0].firstChild.data
            page_link = item.getElementsByTagName('link')[0].firstChild.data
            desc = item.getElementsByTagName('description')[0].firstChild.data
            FeedEntry.objects.create_feedentry(title=title, desc=desc,
                                             page_link=page_link,
                                             pub_date=pub_date, source=url)
    #FIXME:Try to pass only variables accessed in all_feeds_template.
    #Only use locals when too many objects are to be accessed, which wont be
    #the normal case anyway.
    return response(request, all_feeds_template, locals())

def view_homepage(request, homepage_template):
    return response(request, homepage_template, {})

def view_search(request, search_template):
    from feeds.forms import SearchForm
    feedentries = []
    if request.method == 'POST':
        form = SearchForm(post_data(request))
        if form.is_valid():
            query = form.cleaned_data['query']
            if not hasattr(settings, 'SEARCHER') or settings.SEARCHER == 'normal':
                feedentries = FeedEntry.objects.filter(Q(title__icontains=query) | Q(desc__icontains=query))
    else:
        form = SearchForm()
    return response(request, search_template, {'form': form,
                                               'feedentries': feedentries})
    
def view_feedentry_profile(request, feedentry_id, feedentry_slug, feedentry_profile_template):
    feedentry = get_object_or_404(FeedEntry, id=int(feedentry_id))
    return response(request, feedentry_profile_template, {'feedentry': feedentry})

def view_feed_profile(request, feed_id, feed_profile_template):
    feed = get_object_or_404(Feed, id=int(feed_id))
    return response(request, feed_profile_template, {'feed':feed})