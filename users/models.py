from django.db import models

# Create your models here.
class User(models.Model):
    account_id      = models.CharField(max_length=45, unique=True)
    password        = models.CharField(max_length=200)
    name            = models.CharField(max_length=45)
    postal          = models.CharField(max_length=45)
    address         = models.CharField(max_length=50)
    address_detail  = models.CharField(max_length=45)
    phone_number    = models.CharField(max_length=13, unique=True)
    sms_reception   = models.BooleanField(default=False)
    email           = models.EmailField(max_length=45, unique=True)
    email_reception = models.BooleanField(default=False)

    class Meta:
        db_table = 'users'


