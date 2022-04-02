from rest_framework import serializers
from .models import Review
class ReviewSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Review
        fields = ['subject','product_name','product_id','stars','body']