from django.contrib import admin
from .models import Box


class BoxAdmin(admin.ModelAdmin):
    search_fields = ['name']

    class Meta:
        model = Box


admin.site.register(Box, BoxAdmin)
