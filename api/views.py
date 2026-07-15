from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet,ViewSet
from .models import Product
from rest_framework import viewsets
from .seriallizers import ProductSerializer
# Create your views here.

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
