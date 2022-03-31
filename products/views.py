from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer
from django.shortcuts import render

@api_view(['GET','POST'])
def products_list(request):
    product = Product.objects.all()
    if request.method == 'GET':
        serializer = ProductSerializer(product, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProductSerializer(data = request.data)
        if serializer.is_valid() == True:
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        else: 
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)