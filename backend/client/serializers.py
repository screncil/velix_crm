from rest_framework import serializers
from .models import Client, WhereKnow

class WhereKnowSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhereKnow
        fields = '__all__'



class ClientSerializer(serializers.ModelSerializer):
    where_know = WhereKnowSerializer()

    class Meta:
        model = Client
        fields = '__all__'

class AddClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'