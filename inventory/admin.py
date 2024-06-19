from django.contrib import admin
from .models import Item, ItemBase, ItemCode, UOM

admin.site.site_header = "S360 Inventory System"

admin.site.register(Item)
admin.site.register(ItemBase)
admin.site.register(ItemCode)
admin.site.register(UOM)


