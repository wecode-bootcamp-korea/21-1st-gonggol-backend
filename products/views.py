import json

from django.views     import View
from django.http      import JsonResponse
from django.db.models import Q

from products.models import Product, Image, Stock, ProductTag, Tag

class ProductDetailView(View):
    def get(self, request):
        try:
            data1       = json.loads(request.body)
            product     = Product.objects.get(id=data1['product_id'])
            images      = Image.objects.filter(product_id=product.id)
            tags        = ProductTag.objects.filter(product_id=product.id)
            size_stocks = Stock.objects.filter(product_id=product.id)

            if product.discount < 1:
                data = {
                'name'      : product.name,
                'sell_price': float(product.price)*product.discount,
                'con_price' : product.price,
                'body'      : product.body,
                'image'     : [image.url for image in images],
                'tags'      : [tag.tag.name for tag in tags],
                'material'  : product.material,
                'size'      : [size_stock.size.size for size_stock in size_stocks],
                'stock'     : [size_stock.count for size_stock in size_stocks],
            }

            if product.discount == 1:
                data = {
                    'name'     : product.name,
                    'price'    : product.price,
                    'body'     : product.body,
                    'image'    : [image.url for image in images],
                    'tags'     : [tag.tag.name for tag in tags],
                    'material' : product.material,
                    'size'     : [size_stock.size.size for size_stock in size_stocks],
                    'stock'    : [size_stock.count for size_stock in size_stocks],
                }

            return JsonResponse({"result":data}, status = 200)

        except KeyError:
            return JsonResponse({"result":"KEY_ERROR"}, status = 400)

class ProductMainView(View):
    def get(self, request):
        new_tag       = Tag.objects.get(name='신상품')
        best_tag      = Tag.objects.get(name='베스트')
        new_products  = ProductTag.objects.filter(tag_id=new_tag.id)
        best_products = ProductTag.objects.filter(tag_id=best_tag.id)
        new_product_lists  =[]
        best_product_lists =[]

        for new_product in new_products:
            img = Image.objects.get(Q(is_main=True)&Q(product_id=new_product.product.id))
            new_product_list = {
                'name' :new_product.product.name,
                'price':new_product.product.price,
                'img'  :img.url
            }
            new_product_lists.append(new_product_list)

        for best_product in best_products:
            img = Image.objects.get(Q(is_main=True)&Q(product_id=best_product.product.id))
            best_product_list = {
                'name' :best_product.product.name,
                'price':best_product.product.price,
                'img'  :img.url
            }
            best_product_lists.append(best_product_list)

        return JsonResponse({"result":[new_product_lists,best_product_lists]}, status = 200)