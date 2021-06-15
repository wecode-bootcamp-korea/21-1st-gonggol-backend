from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField
from django.db.models.fields.related import ForeignKey

class Order(models.Model):
    user     = models.ForeignKey('users.User', on_delete=models.CASCADE)
    product  = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    size     = models.CharField(max_length=10, null=True)

    class Meta:
        db_table = 'orders'