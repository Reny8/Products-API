from rest_framework.decorators import api_view
from rest_framework.response import Response
from reviews.models import Review
from .serializers import ReviewSerializer
from rest_framework import status
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


@api_view(['GET'])
def review_detail(request,fk):
    
    return Response('review_detail test')