import json

from django.views import View
from django.http  import JsonResponse

from .models         import Order
from users.models    import User
from products.models import Product
from users.utils     import UserInfoDeco

class CartList(View):
    # @UserInfoDeco
    def post(self, request): # 제품에서 장바구니 눌렀을 때, 우선 카트 테이블에 저장
        data     = json.loads(request.body)
        # user     = request.account # token 유저정보
        user     = User.objects.get(account=data['account'])
        product  = Product.objects.get(name=data['product'])
        size     = data['size']
        quantity = data['quantity']

        Order.objects.create(user_id=user.id, product_id=product.id, size=size, quantity=quantity)
        return JsonResponse({"message":"장바구니 생성 성공"}, status=200)

class CartListView(View):
    # @UserInfoDeco
    def POST(self, request):
        # user = request.account
        data = json.loads(request.body)
        user = User.objects.get(account=data['account'])

        order_list = Order.objects.get(user_id=user.id)
        cart = Product.objects.get(id=order_list.product_id)
        order_info = []
        order_info2 = {
            "product_name" : cart.name
        }
        order_info.append(order_info2)
        
        return JsonResponse({"message" : order_info}, status=200)
            