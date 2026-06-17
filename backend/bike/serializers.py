from rest_framework import serializers
from .models import Bike
from sinotrack.serializers import SinotrackSerializer
from sinotrack.models import Sinotrack


class CreateBikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bike
        fields = '__all__'

    def create(self, validated_data):    
        if 'sinotrack' in validated_data:
            bike = Bike.objects.create(**validated_data)
            sinotrack = Sinotrack.objects.get(id=validated_data['sinotrack'].id)
            sinotrack.available = False
            sinotrack.save()
            return bike
        else:
            bike = Bike.objects.create(
                name = validated_data['name'],
                model = validated_data['model'],
                serial_number = validated_data['serial_number'],
                wheel_diameter = validated_data['wheel_diameter'],
                comments = validated_data['comments'],
            )
            return bike

class BikeSerializer(serializers.ModelSerializer):
    sinotrack = SinotrackSerializer()

    class Meta:
        model = Bike
        fields = '__all__'
