import json

from django.http  import JsonResponse
from django.views import View

from users.models import User
from users.validations import validate_email, validate_password

class SignUpView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)

            email    = data['email']
            password = data['password']
            
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
                password     = data['password'],
                email        = email                
            )
            
            return JsonResponse({"message" : "SUCCESS"}, status=201)

        except KeyError:
            return JsonResponse({"message" : "KEY_ERROR"}, status=400)

class SignInView(View):
    def get(self, request):
        try:
            data = json.loads(request.body)

            email    = data['email']
            password = data['password']
            
            if not User.objects.filter(email = email).exists():
                return JsonResponse ({"message" : "INVALID_USER"}, status=401)
            
            if not User.objects.filter(email = email, password = password).exists():
                return JsonResponse ({"message" : "INVALID_USER"}, status=401)
            
            return JsonResponse({"message" : "SUCCESS"}, status=200)

        except KeyError:
            return JsonResponse({"message" : "KEY_ERROR"}, status=400)