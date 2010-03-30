from feedbox.models import FeedEntry, Feed
from utils import response
import urllib
from xml.dom import minidom
        
def view_all_feeds(request, all_feeds_template):
    return response(request, all_feeds_template, {'all_feeds': FeedEntry.objects.all()})

def view_save_feed(request, all_feeds_template):
    for url_obj in Feed.objects.all():
        url = url_obj.source_url
        fp = urllib.urlopen(url)
        xmldoc = minidom.parse(fp)
        xmlitem = xmldoc.getElementsByTagName('item')
        for item in xmlitem:
           title = item.getElementsByTagName('title')[0].firstChild.data
           pub_date = item.getElementsByTagName('pubDate')[0].firstChild.data   
           page_link = item.getElementsByTagName('link')[0].firstChild.data
           desc = item.getElementsByTagName('description')[0].firstChild.data
           FeedEntry.objects.save_feed_entry(title=title,desc=desc,
                                             page_link=page_link,
                                             pub_date=pub_date,source=url)
        #fp.close()
        
    return response(request, all_feeds_template, locals())            