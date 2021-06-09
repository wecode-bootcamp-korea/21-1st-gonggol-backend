from products.models import Product
from django.db import models

from users.models    import User
from products.models import Product

class Order(models.Model):
    user     = models.ForeignKey(User, on_delete=models.CASCADE)
    product  = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    class Meta:
        db_table = 'orders'

        


    