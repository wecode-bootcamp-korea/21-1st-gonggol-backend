from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField
from django.db.models.fields.related import ForeignKey

class Order(models.Model):
    user       = models.ForeignKey('users.User', on_delete=models.CASCADE)
    status     = models.ForeignKey('Status', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'orders'

class OrderItem(models.Model):
    order    = models.ForeignKey('Order', on_delete=CASCADE)
    product  = models.ForeignKey('products.Product', on_delete=CASCADE)
    quantity = models.IntegerField()
    size     = models.CharField(max_length=10, null=True)

    class Meta:
        db_table = 'order_items'

class Status(models.Model):
    status_name = models.CharField(max_length=10)

    class Meta:
        db_table = 'status'