from rest_framework import serializers
from .models import *

class WerehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Werehouse
        fields = "__all__"
        # fields = ["title","location_name","location_url"]

# class CustomerSerializers(serializers.ModelSerializer)       

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
        
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"
        
class DeliverySerializers(serializers.ModelSerializer):
    class Meta:
        model = Delivery
        fields = "__all__"
        
