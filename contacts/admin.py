from django.contrib import admin
from . import models
# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'couch', 'email', 'contact_date')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'email', 'couch')
    list_per_page = 10


admin.site.register(models.Contact, ContactAdmin)
