from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import ClientSerializer, AddClientSerializer, WhereKnowSerializer
from .models import Client, WhereKnow

class AllClientsView(APIView):
    def get(self, request):
        items = Client.objects.all()
        serializer = ClientSerializer(items, many=True)
        return Response(serializer.data)
    

class AddClientView(APIView):
    def post(self, request):
        serializer = AddClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class AllWhereKnow(APIView):
    def get(self, request):
        items = WhereKnow.objects.all()
        serializer = WhereKnowSerializer(items, many=True)
        return Response(serializer.data)