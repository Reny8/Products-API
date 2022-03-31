from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer


@api_view(['GET','POST'])
def products_list(request):
    if request.method == 'GET':
        product = Product.objects.all()
        serializer = ProductSerializer(product, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProductSerializer(data = request.data)
        if serializer.is_valid() == True:
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        else: 
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def product_detail(request,pk):
    # if it does not find a product with that primary key
    try: 
        product = Product.objects.get(pk = pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    except Product.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
