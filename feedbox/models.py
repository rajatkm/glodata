from django.db import models

class FeedURL(models.Model):
    id = models.AutoField(primary_key=True)
    source_url = models.TextField(max_length=150, unique=True, db_index=True)
    source_info = models.TextField(max_length=50)
#    objects = FeedURLModelManager()
    
    def __unicode__(self):
        return self.source_info

class FeedEntryManager(models.Manager):
    def save_feed_entry(self, title, desc, page_link, pub_date, source):
        if not self.exists(feed_page_link=page_link):
            new_feed = FeedEntry(feed_title=title,
                                      feed_desc=desc,
                                      feed_page_link=page_link, 
                                      feed_pub_date=pub_date,
                                      feed_generated_by_url=source)
            new_feed.save()
        return new_feed

    def get_feed_entry(self, title, desc, page_link, pub_date, from_site):
        return super(FeedEntryManager, self).get_query_set()
    
class FeedEntry(models.Model):
    id = models.AutoField(primary_key=True)
    feed_title = models.TextField(max_length=150, unique=True, db_index=True)
    feed_desc = models.TextField(max_length=1000)
    feed_page_link = models.TextField(max_length=100, unique=True, db_index=True)
    feed_generated_by_url = models.ForeignKey(FeedURL)    
    feed_pub_date = models.DateTimeField()    
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    objects = FeedEntryManager()

    class Meta:
        ordering = ['-created_on']
        get_latest_by = 'created_on'

    def __unicode__(self):
        return self.feed_title