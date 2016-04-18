from django.contrib import admin
from lists.models import List, ListItem


@admin.register(List)
class ListAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'name', 'expired',
                    'expiration_date')


@admin.register(ListItem)
class ListItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'name', 'list', 'price', 'amazon_link')


