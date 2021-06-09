import json

from django.http.response import JsonResponse
from django.http import JsonResponse
from django.views import View


class CartList(View):
    def get(self, request):
        return JsonResponse({"a":"b"}, status=200)

