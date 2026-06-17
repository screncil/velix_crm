from rest_framework import serializers
from .models import Sinotrack


class SinotrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sinotrack
        fields = '__all__'