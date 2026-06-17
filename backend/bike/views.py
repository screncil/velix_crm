from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Bike
from .serializers import BikeSerializer, CreateBikeSerializer


class GetAllBikes(APIView):

    def get(self, request):
        items = Bike.objects.all()
        serializer = BikeSerializer(items, many=True)
        return Response(serializer.data)
    

class AddBike(APIView):

    def post(self, request):
        serializer = CreateBikeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
