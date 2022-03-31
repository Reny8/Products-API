from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer
from django.shortcuts import render

@api_view(['GET'])
def products_list(request):
    product = Product.objects.all()
    serializer = ProductSerializer(product, many = True)
    # This takes back all the products created and returns it to python as a dictionary 
    # The response will turn it into a JSON
    return Response(serializer.data)