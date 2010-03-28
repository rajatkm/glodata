from feedbox.models import FeedURLModel
from django.contrib import admin
 
class FeedURLModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {'Feed url': ("url",)}
    list_per_page = 25
    
admin.site.register(FeedURLModel, FeedURLModelAdmin)
