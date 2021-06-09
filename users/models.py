from django.db import models

class User(models.Model):
    account         = models.CharField(max_length=45, unique=True)
    password        = models.CharField(max_length=200)
    name            = models.CharField(max_length=45)
    postal          = models.CharField(max_length=45)
    address         = models.CharField(max_length=50)
    address_detail  = models.CharField(max_length=45)
    phone_number    = models.CharField(max_length=13)
    sms_reception   = models.BooleanField(default=False)
    email           = models.EmailField(max_length=45, unique=True)
    email_reception = models.BooleanField(default=False)
    product         = models.ManyToManyField('products.Product', through='products.Like')

    class Meta:
        db_table = 'users'
