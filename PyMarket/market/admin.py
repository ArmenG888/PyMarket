from django.contrib import admin
from .models import *

class ItemAdmin(admin.ModelAdmin):
    list_display = ("owner", "selling", "price")


admin.site.register(item, ItemAdmin)
admin.site.register(items)