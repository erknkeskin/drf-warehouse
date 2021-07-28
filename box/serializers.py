from rest_framework import serializers
from box.models import Box


class BoxSerializers(serializers.ModelSerializer):
    class Meta:
        model = Box
        fields = '__all__'
