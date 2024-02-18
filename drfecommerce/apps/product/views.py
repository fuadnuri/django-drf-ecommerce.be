from .serializers import (
    BrandSerializer, CategorySerialiser, ProductSerializer)
from .models import (Product, Brand, Category)

from rest_framework.response import Response
from rest_framework import viewsets


class ProductViewSet(viewsets.ViewSet):
    queryset = Product.objects.all()

    def list(self, request):
        serializer = ProductSerializer(self.queryset, many=True)
        return Response(serializer.data)
