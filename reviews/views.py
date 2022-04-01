from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

@api_view(['GET'])
def create_a_review(request):
    
    return Response('test')

# mirror the products functions