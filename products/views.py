
from django.db.models import Q
from django.views     import View
from django.http      import JsonResponse

from products.models import Tag, ProductTag, Image

class ProductMainView(View):
    def get(self, request):
        try:
            new_tag       = Tag.objects.get(name='신상품')
            best_tag      = Tag.objects.get(name='베스트')
            new_products  = ProductTag.objects.filter(tag_id=new_tag.id)
            best_products = ProductTag.objects.filter(tag_id=best_tag.id)
            new_product_lists  =[]
            best_product_lists =[]

            for new_product in new_products:
                img = Image.objects.get(Q(is_main=True)&Q(product_id=new_product.product.id))
                new_product_list = {
                    'new' :[{
                        'name' :new_product.product.name,
                        'price':new_product.product.price,
                        'img'  :img.url
                        }]
                }
                new_product_lists.append(new_product_list)

            for best_product in best_products:
                img = Image.objects.get(Q(is_main=True)&Q(product_id=best_product.product.id))
                best_product_list = {
                    'best' : [{
                        'name' :best_product.product.name,
                        'price':best_product.product.price,
                        'img'  :img.url
                        }]
                    
                }
                best_product_lists.append(best_product_list)
                
            return JsonResponse({"result":[new_product_lists,best_product_lists]}, status = 200)
        
        except KeyError:
            return JsonResponse({"message":"KEY_ERROR"}, status = 400)
