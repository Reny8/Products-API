from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer
from django.shortcuts import get_object_or_404



@api_view(['GET','POST'])
def products_list(request):
    if request.method == 'GET':
        product = Product.objects.all()
        serializer = ProductSerializer(product, many = True)
        return Response(serializer.data, status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = ProductSerializer(data = request.data)
        if serializer.is_valid(raise_exception = True):
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)

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
        serializer = ProductSerializer(product,data = request.data, partial = True)
        if serializer.is_valid(raise_exception = True):
            serializer.save()
            return Response(serializer.data, status = status.HTTP_202_ACCEPTED)

        