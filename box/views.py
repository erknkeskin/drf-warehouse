from rest_framework import viewsets
from box.serializers import Box, BoxSerializers


class BoxViewSet(viewsets.ModelViewSet):
    queryset = Box.objects.all().order_by('-created')
    serializer_class = BoxSerializers
