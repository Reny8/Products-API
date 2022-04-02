from django.db import models
from products.models import Product
# Create your models here.
# Review many to one Product (One product, many reviews)
# when added a new review include the fk of the product
class Review(models.Model):
    product_name = models.CharField(max_length= 50)
    subject = models.CharField(max_length = 50)
    stars = models.DecimalField(max_digits = 2, decimal_places = 1)
    body = models.CharField(max_length = 300)
    product_id = models.IntegerField()



