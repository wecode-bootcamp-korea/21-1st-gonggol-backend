import json

from django.views     import View
from django.http      import JsonResponse

from products.models import Product, Image, Stock, ProductTag

class ProductDetailView(View):
    def get(self, request, product_id):
        try:
            # product_id  = request.GET['product_id']
            product     = Product.objects.get(id=product_id)
            images      = Image.objects.filter(product_id=product.id)
            tags        = ProductTag.objects.filter(product_id=product.id)
            size_stocks = Stock.objects.filter(product_id=product.id)

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

            if product.discount < 1:
                data['sell_price'] = (float(product.price)*product.discount)

            return JsonResponse({"result":data}, status = 200)

        except KeyError:
            return JsonResponse({"result":"KEY_ERROR"}, status = 400)

