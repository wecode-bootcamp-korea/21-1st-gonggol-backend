import json

from django.http.response import JsonResponse
from django.http import JsonResponse
from django.views import View
from users.models import User


class CartList(View):
    def get(self, request): # test
        return JsonResponse({"aa":"bb"}, status=200)