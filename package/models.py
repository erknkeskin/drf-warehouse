from django.db import models
from product.models import Product
from box.models import Box


class Package(models.Model):
    name = models.CharField(max_length=120, verbose_name='Package Name', null=False)
    product = models.ManyToManyField(Product, null=True, related_name='products')
    created = models.DateTimeField(auto_now_add=True, null=False)

    def __str__(self):
        return self.name


class PackageRelation(models.Model):
    class Meta:
        verbose_name_plural = 'Package Relations'

    package = models.ForeignKey(Package, related_name='package', on_delete=models.CASCADE)
    box = models.ForeignKey(Box, related_name='boxes', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, null=False)
