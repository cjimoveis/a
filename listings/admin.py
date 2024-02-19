from django.contrib import admin
from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'city', 'list_date', 'realtor', 'is_published')
    list_display_links = ('id', 'title', 'price')
    list_filter = ('realtor', 'city', 'state')
    list_editable = ('is_published', )
    search_fields = ('title', 'price', 'city', 'state', 'address', 'zipcode', 'description')
    list_per_page = 30

admin.site.register(Listing, ListingAdmin)
