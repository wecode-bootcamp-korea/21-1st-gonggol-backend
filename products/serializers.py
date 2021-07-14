from rest_framework import serializers
from rest_framework.relations import StringRelatedField

from .models import Product, ProductTag, MainCategory, SubCategory, Image, Tag

class MainCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MainCategory
        fields = ['id', 'name']
  
class SubCategorySerializer(serializers.ModelSerializer):
    maincategory = MainCategorySerializer(many=False, read_only=True)
    
    class Meta:
        model  = SubCategory
        fields = ['id', 'name', 'maincategory']

class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model  = Image
        fields = ['url']


class TagSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Tag
        fields = '__all__'

class ProductTagSerializer(serializers.ModelSerializer):
    tag = TagSerializer(many=False, read_only=True)
    
    class Meta:
        model = ProductTag
        fields = ['tag', 'product']

class ProductSerializer(serializers.ModelSerializer):
    image_set      = ImageSerializer(many=True, read_only=True)
    producttag_set = ProductTagSerializer(many=True, read_only=True)
    sub_category   = SubCategorySerializer(many=False, read_only=True)

    class Meta:
        model  = Product
        fields = ['id', 'name', 'price', 'discount', 'producttag_set', 'image_set', 'sub_category']


######################################

# class ProductSerializer(serializers.Serializer):
#     id       = serializers.IntegerField(read_only=True)
#     name     = serializers.CharField(max_length=45)
#     price    = serializers.DecimalField(max_digits=10, decimal_places=3, default=0.00)
#     body     = serializers.URLField(max_length=200)
#     material = serializers.CharField(max_length=100)
#     date     = serializers.DateField()
#     discount = serializers.FloatField(default=1)

#     def create(self, validated_data):
#         return Product.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.name     = validated_data.get('name', instance.name)
#         instance.price    = validated_data.get('price', instance.price)
#         instance.body     = validated_data.get('body', instance.body)
#         instance.material = validated_data.get('material', instance.material)
#         instance.date     = validated_data.get('date', instance.date)
#         instance.discount = validated_data.get('discount', instance.discount)
#         instance.save()

#         return instance


# #### point ######

# ###1. 일반 시리얼라이즈 create,update 구현

# ###2. APIview vs View 차이
# ###3. 일반 serializer post/create, put/update, get()
# ###4. create(input) update(instance, 값(input))
# ###5. serializer vs Modelserializer