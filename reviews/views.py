from rest_framework.decorators import api_view
from rest_framework.response import Response
from reviews.models import Review
from products.models import Product
from .serializers import ReviewSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404
# Create your views here.

@api_view(['GET','POST'])
def reviews_list(request):
    if request.method == 'GET':
        review = Review.objects.all()
        serializer = ReviewSerializer(review,many = True)
        return Response(serializer.data,status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = ReviewSerializer(data = request.data)
        if serializer.is_valid(raise_exception = True):
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)


@api_view(['GET','PUT','DELETE'])
def review_detail(request,pk):
    review = get_object_or_404(Review, pk = pk)
    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data, status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = ReviewSerializer(review, data = request.data)
        if serializer.is_valid(raise_exception = True):
            serializer.save()
            return Response(serializer.data,status.HTTP_200_OK)
    elif request.method == 'DELETE':
        review.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)