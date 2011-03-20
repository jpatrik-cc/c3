from django.contrib import admin
from cococloud.selection.models import Product, ProductArea


class AreasInline(admin.TabularInline):
    model = ProductArea

class ProductAdmin(admin.ModelAdmin):
    inlines = [
        AreasInline,
    ]

admin.site.register(Product, ProductAdmin)
