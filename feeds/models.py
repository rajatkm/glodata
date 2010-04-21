from utils.models import BaseModel
from django.db import models
from django.template.defaultfilters import slugify
from django.template.defaultfilters import striptags

class FeedManager(models.Manager):
    def create_feed(self, url, name):
        feed = self.exists(url=url)
        if not feed:
            feed = Feed(url=url, name=name)
            feed.save()
        return feed

    def exists(self, url):
        try:
            return self.get(url=url)
        except Feed.DoesNotExist:
            return None

class Feed(BaseModel):
    url = models.CharField(max_length=150, unique=True, db_index=True)
    name = models.CharField(max_length=50)
    blocked = models.BooleanField(default=False)
    last_updated = models.DateTimeField(blank=True, null=True)
    objects = FeedManager()

    def __unicode__(self):
        return self.name

    def block(self):
        self.blocked = True
        self.save()
        return self

    def unblock(self):
        self.block = False
        self.save()
        return self

class FeedEntryManager(models.Manager):
    def create_feedentry(self, title, desc, url, feed):
        feedentry = self.exists(url=url)
        if not feedentry:
            title = striptags(title)
            desc = striptags(desc)
            feedentry = FeedEntry(title=title, slug=slugify(title), desc=desc, url=url, feed=feed)
            feedentry.save()
        return feedentry

    def exists(self, url):
        try:
            return self.get(url=url)
        except FeedEntry.DoesNotExist:
            return None

class FeedEntry(BaseModel):
    title = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    desc = models.TextField(max_length=500)
    url = models.CharField(max_length=200, unique=True, db_index=True)
    feed = models.ForeignKey(Feed)
    objects = FeedEntryManager()
    
    class Meta:
        verbose_name_plural = 'Feed Entries'
        verbose_name = "Feed Entry"

    def __unicode__(self):
        return self.title
