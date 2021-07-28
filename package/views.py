from rest_framework import viewsets, status
from rest_framework.response import Response

from package.serializers import PackageSerializers
from product.models import Product
from .models import Package, PackageRelation
from box.models import Box


class PackageViewSet(viewsets.ModelViewSet):
    queryset = Package.objects.all().order_by('-created')
    serializer_class = PackageSerializers

    def create(self, request, *args, **kwargs):
        total_volumes = 0
        for _id in request.data['product']:
            product = Product.objects.filter(id=_id).values()
            total_volumes += (product[0]['length'] * product[0]['width'] * product[0]['height'])

        box = Box.objects.filter(volume__gte=total_volumes).order_by('volume').first()

        if box:
            package = Package.objects.create(name=request.data['name'])
            package.product.set(request.data['product'])
            package.save()

            package_relation = PackageRelation(package=package, box=box)
            package_relation.save()

            data = PackageSerializers(package).data

            return Response(data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
