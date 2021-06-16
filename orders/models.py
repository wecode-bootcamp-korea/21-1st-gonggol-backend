from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField
from django.db.models.fields.related import ForeignKey

class Cart(models.Model):
    user       = models.ForeignKey('users.User', on_delete=models.CASCADE)
    status     = models.ForeignKey('Status', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'carts'

class CartItem(models.Model):
    cart     = models.ForeignKey('Cart', on_delete=CASCADE)
    product  = models.ForeignKey('products.Product', on_delete=CASCADE)
    quantity = models.IntegerField(default=1)
    size     = models.CharField(max_length=10, null=True)

    class Meta:
        db_table = 'cartitems'

class Status(models.Model):
    status_name = models.CharField(max_length=10)

    class Meta:
        db_table = 'status'