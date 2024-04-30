from django.shortcuts import render
from rest_framework import generics

from shop.models import ProductsModel
from shop.serializers import ProductsSerializer


class ProductsListView(generics.ListAPIView):
    queryset = ProductsModel.objects.all()
    serializer_class = ProductsSerializer


class ProductsListCreateView(generics.ListCreateAPIView):
    queryset = ProductsModel.objects.all()
    serializer_class = ProductsSerializer


class ProductsReadUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductsModel.objects.all()
    serializer_class = ProductsSerializer