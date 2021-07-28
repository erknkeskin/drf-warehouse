from django.contrib import admin
from .models import Package, PackageRelation


class PackageAdmin(admin.ModelAdmin):
    search_fields = ['name']

    class Meta:
        model = Package


class PackageRelationAdmin(admin.ModelAdmin):
    class Meta:
        model = PackageRelation


admin.site.register(Package, PackageAdmin)
admin.site.register(PackageRelation, PackageRelationAdmin)
