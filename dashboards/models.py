from utils.models import BaseModel
from django.db import models
from feeds.models import FeedEntry

class UserFeedEntryManager(models.Manager):
    def create_user_feedentry(self, feedentry):
        user_feedentry = self.exists(feedentry = feedentry)
        if not user_feedentry:
            user_feedentry = UserFeedEntry(name='Thilak', feedentry=feedentry)
            user_feedentry.save()
        return user_feedentry

    def exists(self, url):
        try:
            return self.get(url=url)
        except UserFeedEntry.DoesNotExist:
            return None

class UserFeedEntry(BaseModel):
    name = models.CharField(max_length=50)
    feedentry = models.ForeignKey(FeedEntry)
    objects = UserFeedEntryManager()

    def __unicode__(self):
        return self.name