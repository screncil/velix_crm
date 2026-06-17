from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Categories
from .serializers import CategorySerializer


class GetAllCategories(APIView):
    def get(self, request):
        items = Categories.objects.all()
        serializer = CategorySerializer(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)