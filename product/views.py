from rest_framework import viewsets
from product.serializers import Product, ProductSerializers


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('-created')
    serializer_class = ProductSerializers
