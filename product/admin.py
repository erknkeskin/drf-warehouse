from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    search_fields = ['name']

    class Meta:
        model = Product


admin.site.register(Product, ProductAdmin)
