import json
from json.decoder import JSONDecodeError

from django.views import View
from django.http  import JsonResponse

from .models         import Order, OrderItem, Status
from products.models import Product
from users.utils     import UserInfoDeco

class OrderView(View):
    @UserInfoDeco
    def post(self, request):
        try:
            user     = request.user
            data     = json.loads(request.body)
            size     = data['size']
            quantity = data['quantity']

            product = Product.objects.get(id=data['productId'])
            status  = Status.objects.get(id=1)

            cart, created = Order.objects.get_or_create(user_id=user.id, status=status)

            if OrderItem.objects.filter(order_id=cart.id, product_id=product.id, size=size).exists():
                user_order           = OrderItem.objects.get(order_id=cart.id, product_id=product.id, size=size)
                user_order.quantity += int(quantity)
                user_order.save()
                return JsonResponse({"message" : "cart update success"}, status=200)

            OrderItem.objects.create(
            order_id   = cart.id,
            product_id = product.id,
            size       = size,
            quantity   = quantity
            )
            return JsonResponse({"message" : "cart add success"}, status=200)
        except Product.DoesNotExist:
            return JsonResponse({"message" : "INVALID_PRODUCT"}, status=400)
        except KeyError:
            return JsonResponse({"message" : "KEY_ERROR"}, status=400)
        except JSONDecodeError:
            return JsonResponse({'message':'DECODE_ERROR'}, status=400)
            
    @UserInfoDeco
    def get(self, request):
        try:
            user        = request.user
            order       = Order.objects.get(user_id=user.id)
            cart_items  = order.orderitem_set.filter(order_id=order.id)
            
            cartlist = []
            for product_info in cart_items:
                product = Product.objects.get(id=product_info.product_id)
                order_info = {
                    "product_name" : product.name,
                    "option"       : product_info.size,
                    "quantity"     : product_info.quantity,
                    "price"        : product.price,
                    "image"        : product.image_set.get(product_id=product.id).url
                }
                cartlist.append(order_info)
            return JsonResponse({"message" : cartlist}, status=200)
        except Order.DoesNotExist:
            return JsonResponse({"message" : "ORDER_DOSE_NOT_EXIST"}, status=400)

    @UserInfoDeco
    def delete(self, request, productId):
        try:
            user = request.user

            user_info = Order.objects.get(user_id=user.id)
            del_item  = user_info.orderitem_set.get(product_id = productId)
            del_item.delete()
            return JsonResponse({"message" : "success"}, status=200)
        except OrderItem.DoesNotExist:
            return JsonResponse({"message" : "INVALID_productId"}, status=400)
