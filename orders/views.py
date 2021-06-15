import json

from django.views import View
from django.http  import JsonResponse

from .models         import Order
from users.models    import User
from products.models import Product, Image
from users.utils     import UserInfoDeco

class CartView(View):
    @UserInfoDeco
    def post(self, request): # 제품상세에서 장바구니 눌렀을 때, 우선 DB에 저장
        try:
            user     = request.user # token 유저정보
            data     = json.loads(request.body)
            product  = Product.objects.get(id=data['productId'])
            size     = data['size']
            quantity = data['quantity']

            if Order.objects.filter(user_id=user.id, product_id=product.id, size=size).exists(): # 장바구니에 이미 같은 제품이 들어가있다면 갯수만 추가
                user_order           = Order.objects.get(user_id=user.id, product_id=product.id, size=size)
                user_order.quantity += int(quantity)
                user_order.save()
                return JsonResponse({"message":"장바구니 업데이트 성공"}, status=200)
            else: # 아니라면 장바구니 생성
                Order.objects.create(
                    user_id    = user.id,
                    product_id = product.id,
                    size       = size,
                    quantity   = quantity
                    )
                return JsonResponse({"message":"장바구니 생성 성공"}, status=200)
        except Product.DoesNotExist:
            return JsonResponse({"message":"잘못된 product"}, status=500)
            
    @UserInfoDeco
    def get(self, request): # User의 장바구니 프론트단 전달
        user       = request.user
        order_list = Order.objects.filter(user_id=user.id)
        
        cart = []
        for product_info in order_list:
            product = Product.objects.get(id=product_info.product_id)
            order_info = {
                "제품명"       : product.name,
                "옵션"         : product_info.size,
                "수량"         : product_info.quantity,
                "판매가"       : product.price,
                "image"        : product.image_set.get(product_id=product.id).url
            }
            cart.append(order_info)
        return JsonResponse({"message" : cart}, status=200)
            