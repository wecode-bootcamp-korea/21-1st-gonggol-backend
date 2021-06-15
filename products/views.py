import json

from django.core.exceptions  import ObjectDoesNotExist
from django.http             import JsonResponse
from django.views            import View
from django.db.models        import Q

from products.models import Image, MainCategory, Product, ProductTag, SubCategory, Tag

class ProductListView(View):
    def get(self, request):
        try:
            category_id     = request.GET.get('categoryId', None)
            sub_category_id = request.GET.get('subcategoryId', None)
            sort            = request.GET.get('sort-method', None)

            q = Q()
            
            if category_id:
                q &= Q(sub_category__maincategory_id=category_id)
                products = Product.objects.filter(q)

            if sub_category_id:
                q &= Q(sub_category_id=sub_category_id)
                products = Product.objects.filter(q)
            
            if (category_id or sub_category_id) and sort:
                q &= Q(sub_category__maincategory_id=category_id)
                products = Product.objects.filter(q).order_by(sort)

            results = []

            for product in products:
                tags       = ProductTag.objects.filter(product_id=product.id)
                main_image = Image.objects.filter(is_main=False)
                results.append(
                    {
                        "product_id"    : product.id,
                        "product_name"  : product.name,
                        "product_price" : int(product.price),
                        "discount_rate" : product.discount,
                        "product_image" : [img.url for img in main_image],
                        "product_tag"   : [{"new":tag.tag.new, "sale":tag.tag.sale, "best":tag.tag.best} for tag in tags]
                    }
                )
            return JsonResponse({"results": results, "total_counts" : len(results)}, status=200)
        except:
            return JsonResponse({"MESSAGE": "해당 상품이 존재하지 않습니다."}, status=404)
            
            