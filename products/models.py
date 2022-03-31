from django.db import models
# for string use CharField()
# for number use IntegerField()
# for decimal use DecimalField()

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length = 100)
    description = models.CharField(max_length = 100)
    price = models.DecimalField(max_digits = 8,decimal_places = 2)
    inventory_quantity = models.IntegerField()
    