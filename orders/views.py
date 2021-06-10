import json

from django.http.response import JsonResponse
from django.http import JsonResponse
from django.views import View
from users.models import User


class CartList(View):
    def get(self, request):
        return JsonResponse({"a":"b"}, status=200)
    
    def post(self, request):
        data = json.load(request.body)
        user = data['account']
        product = data['product']
        quantity = data['quantity']
