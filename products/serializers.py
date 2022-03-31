# How we define how the outside world can send data to our app. Also helps us to convert JSON to python objects vv
from rest_framework import serializers
from .models import Product
# always name the serializer by the app_name followed by Serializer
# This class will inherit from serializers.ModelSerializer
# Comes with predefined functionality 
# create a class within the class where we define small bits of info about the serializer class
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','title','description','price','inventory_quantity']
