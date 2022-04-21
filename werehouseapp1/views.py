from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework import generics, viewsets


# Create your views here.


class WerehouseListApiView(generics.ListAPIView):
    queryset = Werehouse.objects.all()
    serializer_class = WerehouseSerializer
    
class ProductListAPiView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    
class WerecouseCreateApiView(generics.CreateAPIView):
    queryset = Werehouse.objects.all()
    serializer_class = WerehouseSerializer 
    
class ProductCreateApiView(generics.CreateAPIView):
    queryset = Product
    serializer_class = ProductSerializer    
    


class WerehouseUpdateAPIView(generics.UpdateAPIView):
    queryset = Werehouse.objects.all()
    serializer_class = WerehouseSerializer
    
class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


# class ProductListCreate(generics.ListCreateAPIView):
#     queryset = Product.objects.all()
#     serializers_class = WerehouseSerializer
    
class ProductDeleteAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class WerehouseDeleteAPIView(generics.DestroyAPIView):
    queryset = Werehouse.objects.all()
    serializer_class = WerehouseSerializer

class WerehouseSuperApiview(generics.RetrieveUpdateDestroyAPIView):
    queryset = Werehouse.objects.all()
    serializer_class = WerehouseSerializer