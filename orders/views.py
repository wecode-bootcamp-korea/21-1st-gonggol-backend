import json

from django.views import View
from django.http  import JsonResponse

from .models         import Order, CartItem, Status
from products.models import Product
from users.utils     import UserInfoDeco

class CartView(View):
    @UserInfoDeco
    def post(self, request):
        user     = request.user
        data     = json.loads(request.body)
        size     = data['size']
        quantity = data['quantity']
        product  = Product.objects.get(id=data['productId'])
        status   = Status.objects.get(id=1)
        cart     = Order.objects.filter(user_id=user.id, status=status).first()
        
        if not cart:
            Order.objects.create(user_id=user.id, status=status)  # 유저의 테이블 없다면 생성

        if CartItem.objects.filter(order_id=cart.id, product_id=product.id, size=size).exists(): # 이미 CartItem에 동일 제품이 있다면 갯추만 증가
            user_order           = CartItem.objects.get(order_id=cart.id, product_id=product.id, size=size)
            user_order.quantity += int(quantity)
            user_order.save()
            return JsonResponse({"message":"cart update success"}, status=200)

        CartItem.objects.create(
            order_id   = cart.id,
            product_id = product.id,
            size       = size,
            quantity   = quantity
            )
        return JsonResponse({"message":"cart add success"}, status=200)

    @UserInfoDeco
    def get(self, request): # User의 장바구니 프론트단 전달
        try:
            user        = request.user
            order       = Order.objects.get(user_id=user.id)
            cart_items  = order.cartitem_set.filter(order_id=order.id)
            
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
    def delete(self, request, productId): # 프론트로부터 입력받은 유저의 특정 제품, 장바구니에서 삭제
        try:
            user    = request.user

            user_info = Order.objects.get(user_id=user.id)
            del_item  = user_info.cartitem_set.get(product_id = productId)
            del_item.delete()
            return JsonResponse({"message" : "success"}, status=200)
        except CartItem.DoesNotExist:
            return JsonResponse({"message" : "INVALID_productId"}, status=400)
