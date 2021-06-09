import json, bcrypt, jwt, re

from django.views           import View
from django.http            import JsonResponse
from django.db              import IntegrityError
from django.core.exceptions import ObjectDoesNotExist

from gonggol.settings import SECRET_KEY, ALGORITHM
from .models import User

class JoinIn(View):
    def post(self, request):
        try:
            data            = json.loads(request.body)
            account         = data['account']
            password        = data['password']
            name            = data['name']
            postal          = data['postal']
            address         = data['address']
            address_detail  = data['address_detail']
            phone_number    = data['phone_number']
            sms_reception   = data['sms_reception']
            email           = data['email']
            email_reception = data['email_reception']

            email_regex   = '^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
            pw_regex      = '^[A-Za-z0-9@#$!]{8,12}$'
            account_regex = '^[A-Za-z0-9]{8,12}$'

            if not re.match(account_regex, account):
                return JsonResponse({"message":"id 형식을 확인하세요."}, status=400)
            elif not re.match(pw_regex, password):
                return JsonResponse({"message":"password 형식을 확인하세요."}, status=400)
            if not re.match(email_regex, email):
                return JsonResponse({"message":"email 형식을 확인하세요."}, status=400)

            User.objects.create(
            account         = account,
            password        = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8'),
            name            = name,
            postal          = postal,
            address         = address,
            address_detail  = address_detail,
            phone_number    = phone_number,
            sms_reception   = sms_reception,
            email           = email,
            email_reception = email_reception,
            )
            return JsonResponse({"message":"SUCCESS!"}, status=200)
        except IntegrityError:
            return JsonResponse({"message":"ID나 email중복입니다."}, status=400)
        except KeyError:
            return JsonResponse({"message":"필수 입력 항목을 확인하세요."}, status=400)

class LogIn(View):
    def post(self, request):
        try:
            data     = json.loads(request.body)
            account  = data['account']
            input_password = data['password'].encode('utf-8')

            if account == "" or input_password == "":
                return JsonResponse({"message":"id나 password를 확인하세요."}, status=401)

            login_user = User.objects.get(account=account)
            db_password = login_user.password.encode('utf-8')

            if not bcrypt.checkpw(input_password, db_password):
                return JsonResponse({"message":"id나 password를 확인하세요."}, status=400)

            token     = jwt.encode({"user_id" : login_user.account}, SECRET_KEY, algorithm=ALGORITHM)
            return JsonResponse({"token" : token, "message" : "SUCCESE!"}, status=200)

        except ObjectDoesNotExist:
            return JsonResponse({"message":"id나 password를 확인하세요."}, status=401)
        except KeyError: # id나 password가 입력 없을 때
            return JsonResponse({"message":"id나 password를 확인하세요."}, status=401)