import json
from django.core.exceptions import ObjectDoesNotExist

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
        # sub 카테고리 별 상품 list 
        try:
            sub_category_name = request.GET['name']
            sub_category      = SubCategory.objects.get(name=sub_category_name)
            products          = Product.objects.filter(sub_category_id=sub_category.id)
            main_image        = Image.objects.filter(is_main=True)
        
            product_list_info = []
            for product in products:
                tags = ProductTag.objects.filter(product_id=product.id)
                product_list_info.append(
                    {
                        "product_name"  : product.name,
                        "product_price" : product.price,
                        "sale_price"    : float(product.price) * product.discount,
                        "product_image" : [img.url for img in main_image],
                        "product_tag"   : [tag.tag.name for tag in tags]
                    }
                )
        
            return JsonResponse({'Product_list': product_list_info}, status=200)
        except ObjectDoesNotExist:
            return JsonResponse({'MESSAGE': 'NONE CATEGORY'}, status=404)
