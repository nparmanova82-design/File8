from django.shortcuts import render
from .models import Product
from .seriallizers import ProductSerializer
from rest_framework.generics import ListAPIView,CreateAPIView, UpdateAPIView, RetrieveAPIView, RetrieveUpdateAPIView, DestroyAPIView
from rest_framework import viewsets

class CreateProductView(CreateAPIView):
    serializer_class=ProductSerializer
    queryset=Product.objects.all()

class ProductListAPIView(ListAPIView):
    serializer_class=ProductSerializer
    queryset=Product.objects.all()

class ProductRetrieveAPIView(RetrieveAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer

class ProductUpdateAPIView(UpdateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer

class ProductDestroyAPIView(DestroyAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer

class ProductRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer