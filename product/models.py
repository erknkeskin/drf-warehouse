from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=120, verbose_name='Product Name', null=False)
    width = models.IntegerField(verbose_name='Width', null=False)
    height = models.IntegerField(verbose_name='Height', null=False)
    length = models.IntegerField(verbose_name='Length', null=False)
    created = models.DateTimeField(auto_now_add=True, null=False)

    def __str__(self):
        return self.name
