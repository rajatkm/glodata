from django.contrib import admin
from feedbox.models import Feed
 
class FeedModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {'Feed url': ("url",)}
    list_per_page = 25
    
admin.site.register(Feed, FeedModelAdmin)