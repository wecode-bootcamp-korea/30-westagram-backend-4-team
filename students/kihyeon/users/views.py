import json, bcrypt

from django.http  import JsonResponse
from django.views import View

from users.models import User
from users.validators import validate_email, validate_password

class SignUpView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)

            email           = data['email']
            password        = data['password']
            phone_number    = data['phone_number']
            secret_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            hassed_password = secret_password.decode('utf-8')

            if not validate_email(email):
                return JsonResponse({'Message' : 'Invalid Email'}, status = 400)
            
            if not validate_password(password):
                return JsonResponse({'Message' : 'Invalid Password'}, status = 400)
            
            if User.objects.filter(email = email).exists():
                return JsonResponse({'Message' : 'Email Already Exists'}, status = 400)

            User.objects.create(
                first_name   = data["first_name"],
                last_name    = data["last_name"],
                email        = email,
                password     = hassed_password,
                phone_number = phone_number,
                
            )
            return JsonResponse({"MESSAGE": "User Created!"}, status=201)

        except KeyError:
            return JsonResponse({"MESSAGE": "KEY_ERROR"}, status=400)

class LoginView(View):
    def post(self, request):
        try:
            data     = json.loads(request.body)
            email    = data['email']
            password = data['password']

            if not User.objects.filter(email = email, password = password).exists():
                return JsonResponse({"message" : "INVALID_UESR"}, status = 401)

            return JsonResponse({'MESSAGE' : 'SUCCESS'}, status=200)
            
        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)

