import json

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
                'main_cate'    : product.sub_category.maincategory.name,
                'sub_cate'     : product.sub_category.name,
                'product_id'   : product.id,
                'product_name' : product.name,
                'product_price': int(product.price),
                'body'         : product.body,
                'product_image': [image.url for image in images],
                'tags'         : [{'new':tag.tag.new, 'sale':tag.tag.sale, 'best':tag.tag.best} for tag in tags],
                'material'     : product.material,
                'size_option'  : [{'option_stock':size_stock.count,'option_name':size_stock.size.size} for size_stock in size_stocks]
            }

            if product.discount < 1:
                data['selling_rate'] = product.discount

            return JsonResponse({"result":data}, status = 200)

        except KeyError:
            return JsonResponse({"result":"KEY_ERROR"}, status = 400)

