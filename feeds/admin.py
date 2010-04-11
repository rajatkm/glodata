from django.contrib import admin
from feeds.models import Feed, FeedEntry

class FeedModelAdmin(admin.ModelAdmin):
    list_per_page = 25

class FeedEntryModelAdmin(admin.ModelAdmin):
    list_per_page = 25

admin.site.register(FeedEntry, FeedEntryModelAdmin)
admin.site.register(Feed, FeedModelAdmin)