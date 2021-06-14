
from django.db.models import Q
from django.views     import View
from django.http      import JsonResponse

from products.models import Tag, ProductTag, Image

class ProductMainView(View):
    def get(self, request):
        new_tags       = Tag.objects.filter(new=True)
        best_tags      = Tag.objects.filter(best=True)
        new_product_lists  =[]
        best_product_lists =[]
        
        for new_tag in new_tags:
            new_products  = ProductTag.objects.filter(tag_id=new_tag.id)
            for new_product in new_products:
                img = Image.objects.get(Q(is_main=True)&Q(product_id=new_product.product.id))
                new_product_list = {
                        'product_id'   :new_product.product.id,
                        'product_name' :new_product.product.name,
                        'product_price':int(new_product.product.price),
                        'product_image':img.url
                        }
                new_product_lists.append(new_product_list)

        for best_tag in best_tags :
            best_products = ProductTag.objects.filter(tag_id=best_tag.id)
            for best_product in best_products:
                img = Image.objects.get(Q(is_main=True)&Q(product_id=best_product.product.id))
                best_product_list = {
                        'product_id'   :best_product.product.id,
                        'product_name' :best_product.product.name,
                        'product_price':int(best_product.product.price),
                        'product_image':img.url
                        }

                best_product_lists.append(best_product_list)
        return JsonResponse({"result":{"new_product":new_product_lists,"best_product":best_product_lists}}, status = 200)

