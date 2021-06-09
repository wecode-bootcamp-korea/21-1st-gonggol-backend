## merge 되면 복사해놓기
import Json

from django.db.models.fields import json
from django.http  import JsonResponse
from django.views import View

from products.models import Product, SubCategory, Tag

# ### main 카테고리 이름 
# class MainCategoryList(View):
#     def get(self, request):
#         data           = json.loads(request.body)
#         maincategories = MainCategory.objects.all()

#         main_category = []
#         for maincategory in maincategories:
#             main_category.append(
#                 {
#                     'name': maincategory.name
#                 }
#             )
#         return JsonResponse({'MESSAGE': main_category}, status=200)

# ### sun 카테고리 이름        
# class SubCategoryList(View):
#     def get(self, request):
#         data           = json.loads(request.body)
#         subcategories  = SubCategory.objects.all()

#         sub_category = []
#         for subcategory in subcategories:
#             sub_category.append(
#                 {
#                     'name': subcategory.maincategory.name
#                 }
#             )
#         return JsonResponse({'MESSAGE': sub_category}, status=200)

 ### 해당 상품 리스트

 # 1. 이미지
 # 2. 신상품, 세일, 베스트 태그
 # 3. 상품 이름
 # 4. 가격 / 세일 :      
class ProductList(View):
    def get(self, request):
        data       = json.loads(request.body)
        products   = Product.objects.all()

        product_list = []
        for product in products:
            img = product.object.filter(product_id=product.id)
            if img.is_main:
                if product.tag_set.name:
                    product_list.append(
                        {
                            "name"  : product.name,
                            "price" : product.price,
                            "tag"   : product.tag_set.name,
                            "img"   : img.url
                        }
                    )

        
        
        
        
        
