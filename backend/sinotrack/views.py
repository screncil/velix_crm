from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status 
from .serializers import SinotrackSerializer
from rest_framework.response import Response
from .models import Sinotrack


class GetAllSinotracksAPI(APIView):
    
    def get(self, request):
        items = Sinotrack.objects.all()
        serializer = SinotrackSerializer(items, many=True)
        return Response(serializer.data)
    
class CreateSinotrackView(APIView):

    def post(self, request):
        serializer = SinotrackSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    

class GetAvailableSinotracks(APIView):

    def get(self, request):
        items = Sinotrack.objects.filter(available=True)
        serializer = SinotrackSerializer(items, many=True)
        return Response(serializer.data)