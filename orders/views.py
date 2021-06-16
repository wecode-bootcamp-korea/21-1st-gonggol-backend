import json

from django.views import View
from django.http  import JsonResponse

from .models         import Cart, CartItem, Status
from products.models import Product
from users.utils     import UserInfoDeco

class CartView(View):
    @UserInfoDeco
    def post(self, request):
        user     = request.user
        data     = json.loads(request.body)
        product  = Product.objects.get(id=data['productId'])
        size     = data['size']
        quantity = data['quantity']
        status   = Status.objects.get(id=1)
        
        if not Cart.objects.get(user_id=user.id, status=status): # 결제대기중인 해당유정의 cart테이블 찾기
            Cart.objects.create(user_id=user.id, status=status)  # 없다면 생성

        cart = Cart.objects.get(user_id=user.id, status=status)

        if CartItem.objects.filter(cart_id=cart.id, product_id=product.id, size=size).exists(): # 이미 CartItem에 동일 제품이 있다면 갯추만 증가
            user_order           = CartItem.objects.get(cart_id=cart.id, product_id=product.id, size=size)
            user_order.quantity += int(quantity)
            user_order.save()
            return JsonResponse({"message":"cart update success"}, status=200)
        else: # 아니라면 CartItem 생성
            CartItem.objects.create(
                cart_id    = cart.id,
                product_id = product.id,
                size       = size,
                quantity   = quantity
                )
            return JsonResponse({"message":"cart add success"}, status=200)

    @UserInfoDeco
    def get(self, request): # User의 장바구니 프론트단 전달
        user       = request.user
        cart       = Cart.objects.get(user_id=user.id)
        cart_items  = cart.cartitem_set.filter(cart_id=cart.id)
        
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

    @UserInfoDeco
    def delete(self, request): # 프론트로부터 입력받은 유저의 특정 제품, 장바구니에서 삭제
        user    = request.user
        data    = json.loads(request.body)
        product = data["productId"]

        user_info = Cart.objects.get(user_id=user.id)
        del_item  = user_info.cartitem_set.filter(product_id = product)
        del_item.delete()
        return JsonResponse({"message" : "success"}, status=200)

