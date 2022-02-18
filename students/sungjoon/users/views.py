import json
import re

from django.http  import JsonResponse
from django.views import View

from users.models import User
from users.validations import validate_email, validate_password

class UserView(View):
    def post(self, request):
        data = json.loads(request.body)

        email    = data['email']
        password = data['password']

        try:
            if not validate_email(email):
                return JsonResponse ({"message" : "INVALID_EMAIL"}, status=400)

            if not validate_password(password):
                return JsonResponse ({"message" : "INVALID_PASSWORD"}, status=400)
            
            if User.objects.filter(email = email).exists():
                return JsonResponse ({"message" : "EMAIL_OCCUPIED"}, status=409)
            
            User.objects.create(
                username     = data['username'],
                first_name   = data['first_name'],
                last_name    = data['last_name'],
                phone_number = data['phone_number'],
                password     = password,
                email        = email                
            )
            
            return JsonResponse({"message" : "SUCCESS"}, status=201)

        except KeyError:
            return JsonResponse({"message" : "KEY_ERROR"}, status=400)