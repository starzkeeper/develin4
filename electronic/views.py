from django.shortcuts import render
from rest_framework import generics,viewsets
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Product, Category
from .permissions import IsAdminOrRead
from .serializers import ProductSerializer

class ProductPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 10000

class ProductAPIView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ProductPagination

    @action(methods=['get'],detail=False)
    def category(self,request):
        cats = Category.objects.all()
        return Response({'cats': [c.name for c in cats]})
    def get_permissions(self):
        if self.action == 'get' or 'create':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]












