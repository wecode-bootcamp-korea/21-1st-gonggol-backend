import json

from django.db.models.fields import json
from django.http             import JsonResponse
from django.views            import View
from django.db.models        import Q

from products.models import Image, Product, ProductTag, SubCategory, Tag

### 상품 리스트 / sub카테고리 별로 get 로직 
 # 1. 이미지
 # 2. 신상품, 세일, 베스트 태그
 # 3. 상품 이름
 # 4. 가격 / 세일 :

 ## 백팩 상품 list 
class ProductListView(View):
    def get(self, request):
        sub_name              = SubCategory.objects.get(name="백팩")
        backpack_name         = Product.objects.filter(sub_category_id=sub_name.id)
        main_img              = Image.objects.filter(is_main=False)
        
        backpack_product_info = []
        for backpack_product in backpack_name:
            tags = ProductTag.objects.filter(product_id=backpack_product.id)
            backpack_product_info.append(
                {
                    "product_name"  : backpack_product.name,
                    "product_price" : backpack_product.price,
                    "retail_price"  : float(backpack_product.price) * backpack_product.discount,
                    "product_image" : [img.url for img in main_img],
                    "product_tag"   : [tag.tag.name for tag in tags]
                }
            )
        
        return JsonResponse({'Product_list': backpack_product_info}, status=200)
