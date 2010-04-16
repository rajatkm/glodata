from django.contrib import admin
from feeds.models import Feed, FeedEntry

class FeedModelAdmin(admin.ModelAdmin):
    list_per_page = 25
    list_display = ('name','url', 'blocked')
    search_fields = ('name',)
    list_filter = ('blocked',)

class FeedEntryModelAdmin(admin.ModelAdmin):
    list_per_page = 25
    prepopulated_fields = {'slug': ("title",)}
    list_display = ('title','feed')
    search_fields = ('title', 'slug')
    list_filter = ('feed',)

admin.site.register(FeedEntry, FeedEntryModelAdmin)
admin.site.register(Feed, FeedModelAdmin)