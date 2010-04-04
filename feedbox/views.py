from feedbox.models import FeedEntry, Feed
from utils import response
from xml.dom import minidom
import urllib

def view_all_feeds(request, all_feeds_template):
    return response(request, all_feeds_template, {'all_feeds': FeedEntry.objects.all()})

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