from django.db import models
from products.models import Product
# Create your models here.
# Review many to one Product (One product, many reviews)
# when added a new review include the fk of the product
class Review(models.Model):
    subject = models.CharField(max_length = 50)
    body = models.CharField(max_length = 300)
    



