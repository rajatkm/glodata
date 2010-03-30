from django.db import models
from utils.models import BaseModel
#FIXME:Always have django imports on top of project imports

class FeedManager(models.Manager):
    raise NotImplementedError

class Feed(BaseModel):
    url = models.TextField(max_length=150, unique=True, db_index=True)
    name = models.TextField(max_length=50)
    objects = FeedManager()

    def __unicode__(self):
        return self.name

class FeedEntryManager(models.Manager):
    def save_feed_entry(self, title, desc, url, pub_date):
        #FIXME: What is self.exists returns True? you get 'new_feed' unbound error right ?
        if not self.exists(url=url):
            new_feed = FeedEntry(title=title,
                                desc=desc,
                                url=url,
                                #FIXME:Check my comment on this 'feed_pub_date'
                                #model attribute inside the model
                                feed_pub_date=pub_date)
            new_feed.save()
        #FIXME: What is self.exists returns True? you get 'new_feed' unbound error right ?
        return new_feed

    #FIXME:This is like the ordinary queryset. This does all the things, which
    #normal queryset does. Meaning, how does FeedEntry.objects.get_feed_entry
    #differentiate from FeedEntry.objects.get
    def get_feed_entry(self, title, desc, page_link, pub_date, from_site):
        return super(FeedEntryManager, self).get_query_set()

class FeedEntry(BaseModel):
    title = models.TextField(max_length=150, unique=True, db_index=True)
    desc = models.TextField(max_length=1000)
    url = models.TextField(max_length=100, unique=True, db_index=True)
    feed = models.ForeignKey(Feed)
    #FIXME:Why is feed_pub_date defined in FeedEntry ? whats its use ?
    #Isn't it same as 'created_on' attribute value ?
    #P.S:We can have 'last_updated_date' in Feed Model.     
    feed_pub_date = models.DateTimeField()
    objects = FeedEntryManager()

    class Meta:
        ordering = ['-created_on']
        get_latest_by = 'created_on'

    def __unicode__(self):
        return self.title
