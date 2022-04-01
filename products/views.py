import string
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer
from django.shortcuts import get_object_or_404
from django.db import models

@api_view(['GET','POST'])
def products_list(request):
    if request.method == 'GET':
        product = Product.objects.all()
        serializer = ProductSerializer(product, many = True)
        return Response(serializer.data, status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = ProductSerializer(data = request.data)
        if serializer.is_valid() == True:
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        else: 
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE','PATCH'])
def product_detail(request,pk):
    product = get_object_or_404(Product, pk = pk)
    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data,status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = ProductSerializer(product, data = request.data)
        if serializer.is_valid() == True:
            serializer.save()
            return Response(serializer.data, status.HTTP_200_OK)
    elif request.method == 'DELETE':
        product.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
    elif request.method == 'PATCH':
        # added a photo to the laptop product
        if product.pk == 2:
            product.description += 'Link: https://cdn.mos.cms.futurecdn.net/7WbSVGBMTEaXqu4XNVkX8N-768-80.jpg'
            return Response(product.description)
        else:
            return Response(status = status.HTTP_400_BAD_REQUEST)