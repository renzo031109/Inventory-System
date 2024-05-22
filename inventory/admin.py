from django.contrib import admin
from .models import Item, ItemName

admin.site.site_header = "S360 Inventory System"

admin.site.register(Item)
admin.site.register(ItemName)

