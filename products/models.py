from django.db                       import models
from django.db.models.aggregates     import Count
from django.db.models.deletion       import CASCADE
from django.db.models.fields         import IntegerField

class MainCategory(models.Model):
    name         = models.CharField(max_length=50)
    created_at   = models.DateTimeField(auto_now_add=True)
    updated_at   = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'maincategories'

class SubCategory(models.Model):
    name         = models.CharField(max_length=50)
    maincategory = models.ForeignKey('MainCategory', on_delete=models.CASCADE)
    created_at   = models.DateTimeField(auto_now_add=True)
    updated_at   = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'subcategories'

class Product(models.Model):
    sub_category = models.ForeignKey('SubCategory', on_delete=models.CASCADE)
    name         = models.CharField(max_length=45, unique=True)
    price        = models.DecimalField(max_digits=10, decimal_places=3, default=0.00)
    body         = models.URLField(max_length=200)
    material     = models.CharField(max_length=100)
    date         = models.DateField()
    discount     = models.FloatField(default=1)
    created_at   = models.DateTimeField(auto_now_add=True)
    updated_at   = models.DateTimeField(auto_now=True)
    is_deleted   = models.BooleanField(default=False)
    
    class Meta:
        db_table = 'products'

class Image(models.Model):
    url       = models.URLField(max_length=200)
    product   = models.ForeignKey('Product', on_delete=models.CASCADE)
    is_main   = models.BooleanField(default=False)
    
    class Meta:
        db_table = 'images'

class Size(models.Model):
    size    = models.CharField(max_length=30)
    product = models.ManyToManyField('Product', through='Stock')
    
    class Meta:
        db_table = 'sizes'

class Stock(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    size    = models.ForeignKey('Size', on_delete=models.CASCADE)
    count   = models.IntegerField()

    class Meta:
        db_table = 'stocks'

class Tag(models.Model):
    new     = models.BooleanField(default=False)
    best    = models.BooleanField(default=False)
    sale    = models.BooleanField(default=False)
    product = models.ManyToManyField('Product', through='ProductTag')

    class Meta:
        db_table = 'tags'

class ProductTag(models.Model):
    tag     = models.ForeignKey('Tag', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)

    class Meta:
        db_table = 'product_tags'

class Like(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    user    = models.ForeignKey('users.User', on_delete=models.CASCADE)

    class Meta:
        db_table = 'likes'
