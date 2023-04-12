from django.contrib import admin
from . import models


# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('product_name',)}
    list_display = ('product_name', 'price', 'category', 'modified_date', 'is_available')

admin.site.register(models.Product, ProductAdmin)


class VariationAdmin(admin.ModelAdmin):
    list_display = ('product', 'category', 'value', 'is_available')
    list_filter = ('product', 'category', 'value', 'is_available')
    list_editable = ('is_available',)

admin.site.register(models.Variation,VariationAdmin)
