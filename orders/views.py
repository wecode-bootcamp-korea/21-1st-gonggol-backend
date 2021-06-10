import json

from django.http.response import JsonResponse
from django.http import JsonResponse
from django.views import View
from users.models import User
from products.models import Product


class CartList(View):
    # def get(self, request): # test
        # return JsonResponse({"aa":"bb"}, status=200)

    def post(self, request):
        data = json.load(request.body)
        product = data['name']

        products = Product.objects.get(name=product)
        return JsonResponse({
            "이미지":products.image_set.url
        })
