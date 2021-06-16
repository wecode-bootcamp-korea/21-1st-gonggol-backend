import json

from django.db.models import Q
from django.views     import View
from django.http      import JsonResponse

from products.models import Product, Image, Stock, ProductTag

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

class ProductMainView(View):
    def get(self, request):
        new_products  = ProductTag.objects.filter(tag__new=1)
        best_products = ProductTag.objects.filter(tag__best=1)
        new_product_lists  =[]
        best_product_lists =[]
        
        for new_product in new_products:
            img = Image.objects.get(Q(is_main=True)&Q(product_id=new_product.product.id))
            new_product_list = {
                    'product_id'   :new_product.product.id,
                    'product_name' :new_product.product.name,
                    'product_price':int(new_product.product.price),
                    'product_image':img.url
                    }
            new_product_lists.append(new_product_list)

        for best_product in best_products:
            img = Image.objects.get(Q(is_main=True)&Q(product_id=best_product.product.id))
            best_product_list = {
                    'product_id'   :best_product.product.id,
                    'product_name' :best_product.product.name,
                    'product_price':int(best_product.product.price),
                    'product_image':img.url
                    }

            best_product_lists.append(best_product_list)
        return JsonResponse({"result":{"new":new_product_lists[:18],"best":best_product_lists[:6]}}, status = 200)
