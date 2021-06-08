from django.db import models
from django.db.models.aggregates import Count
from django.db.models.deletion import CASCADE
from django.db.models.fields import IntegerField
from django.db.models.fields.related import OneToOneField

class MainCategory(models.Model):
    name       = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'maincategories'

class SubCategory(models.Model):
    name = models.CharField(max_length=50)
    maincategory = models.ForeignKey(MainCategory, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'subcategories'

class Product(models.Model):
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    name         = models.CharField(max_length=45, unique=True)
    price        = models.DecimalField(max_digits=10, decimal_places=3)
    body         = models.URLField(max_length=200)
    material     = models.CharField(max_length=100)
    data         = models.DateField(auto_now_add=True)
    discount     = models.FloatField(default=1)
    like         = models.BooleanField(default=False)
    created_at   = models.DateTimeField(auto_now_add=True)
    updated_at   = models.DateTimeField(auto_now_add=True)
    is_deleted   = models.BooleanField(default=False)
    
    class Meta:
        db_table = 'products'

class Image(models.Model):
    image_url = models.URLField(max_length=200)
    product   = models.ForeignKey(Product, on_delete=models.CASCADE)
    is_main   = models.BooleanField(default=False)
    
    class Meta:
        db_table = 'images'

class Size(models.Model):
    size    = models.CharField(max_length=30)
    product = models.ManyToManyField(Product, through='Stock')
    
    class Meta:
        db_table = 'sizes'

class Stock(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    size    = models.ForeignKey(Size, on_delete=models.CASCADE)
    count   = models.IntegerField()

    class Meta:
        db_table = 'stocks'

class Tag(models.Model):
    name    = models.IntegerField()
    product = models.ManyToManyField(Product)

    class Meta:
        db_table = 'tags'
        