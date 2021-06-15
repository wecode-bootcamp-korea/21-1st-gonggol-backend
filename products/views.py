import json

from django.views     import View
from django.http      import JsonResponse
from django.db.models import Q

from products.models import Product, Image, Stock, ProductTag, MainCategory, SubCategory, Tag

class ProductDetailView(View):
    def get(self, request, product_id):
        try:
            product     = Product.objects.get(id=product_id)
            images      = Image.objects.filter(product_id=product.id)
            tags        = ProductTag.objects.filter(product_id=product.id)
            size_stocks = Stock.objects.filter(product_id=product.id)

            data = {
                'main_category': product.sub_category.maincategory.name,
                'sub_category' : product.sub_category.name,
                'product_id'   : product.id,
                'product_name' : product.name,
                'product_price': int(product.price),
                'produrct_body': product.body,
                'product_image': [image.url for image in images],
                'product_tag'  : [{'new':tag.tag.new, 'sale':tag.tag.sale, 'best':tag.tag.best} for tag in tags],
                'product_mat'  : product.material,
                'produect_size': [{'option_stock':size_stock.count,'option_name':size_stock.size.size} for size_stock in size_stocks]
            }

            if product.discount < 1:
                data['discount_rate'] = product.discount

            return JsonResponse({"result":data}, status = 200)

        except KeyError:
            return JsonResponse({"result":"KEY_ERROR"}, status = 400)

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
                # main_image = Image.objects.filter(is_main=True)
                main_image = product.image_set.all()
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