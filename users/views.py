import json

from django.views import View
from django.http  import JsonResponse

from .models import User


class Signup(View):
    def post(self, request):
        data            = json.loads(request.body)
        name            = data['name']
        user_id         = data['user_id']
        password        = data['password']
        post_add        = data['post_add']
        address         = data['address']
        address_detail  = data['address_detail']
        phone_number    = data['phone_number']
        sms_reception   = data['sms_reception']
        email           = data['email']
        email_reception = data['email_reception']

        User.objects.create(
        name            = name,
        user_id         = user_id,
        password        = password,
        post_add        = post_add,
        address         = address,
        address_detail  = address_detail,
        phone_number    = phone_number,
        sms_reception   = sms_reception,
        email           = email,
        email_reception = email_reception
        )
        
        return JsonResponse({'MESSAGE': 'SUCCESS'}, status=200)
        
