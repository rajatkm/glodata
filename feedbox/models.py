from utils.models import BaseModel
from django.db import models
#FIXME:Always have django imports on top of project imports
#Ans:Moved

class FeedManager(models.Manager):
    raise NotImplementedError

class Feed(BaseModel):
    url = models.TextField(max_length=150, unique=True, db_index=True)
    name = models.TextField(max_length=50)
    last_updated_date = models.DateTimeField()
    objects = FeedManager()

    def __unicode__(self):
        return self.name

class FeedEntryManager(models.Manager):
    def save_feed_entry(self, title, desc, url, pub_date):
        #FIXME: What is self.exists returns True? you get 'new_feed' unbound error right ?
        new_feed = self.exists(url=url)
        if not news_feed:
            new_feed = FeedEntry(title=title,
                                desc=desc,
                                url=url)
                                #FIXME:Check my comment on this 'feed_pub_date'
                                #model attribute inside the model
                                #Ans:Removed
            new_feed.save()
        #FIXME: What is self.exists returns True? you get 'new_feed' unbound error right ?
        #Ans:Is this fix ok?
        return new_feed

    #FIXME:This is like the ordinary queryset. This does all the things, which
    #normal queryset does. Meaning, how does FeedEntry.objects.get_feed_entry
    #differentiate from FeedEntry.objects.get
    #Ans: No difference to me, so can be removed. If needed we can simply call 
    #FeedEntry.objects.get method from view, right? If so can be removed.
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
    #Ans: Removed as discussed and added a new field 'last_updated_date' in Feed Model
    #Corrected the FeedEntry Object creation too.     
    objects = FeedEntryManager()

    class Meta:
        ordering = ['-created_on']
        get_latest_by = 'created_on'

    def __unicode__(self):
        return self.title
