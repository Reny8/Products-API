from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.models import Product
# Create your views here.

@api_view(['GET'])
def reviews_list(request):
    
    return Response('review_list test')


@api_view(['GET'])
def review_detail(request,fk):
    
    return Response('review_detail test')