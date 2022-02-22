import json, bcrypt, jwt

from django.http  import JsonResponse
from django.views import View

from users.models     import User
from users.validators import validate_email, validate_password
from secret           import ALGORITHM
from config.settings  import SECRET_KEY

class SignUpView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)

            email        = data['email']
            password     = data['password']
            phone_number = data.get('phone_number', '')
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

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
                password     = hashed_password,
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
            user     = User.objects.get(email=email) 

            if not bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
                return JsonResponse({"message" : "WRONG_PASSWORD"}, status = 401)

            access_token = jwt.encode({'id' : user.id}, SECRET_KEY, ALGORITHM)
            return JsonResponse({"message" : "LOGIN_SUCCESS! JWT: " + access_token}, status = 201)
            
        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)
        
        except User.DoesNotExist:
            return JsonResponse({"message" : "INVALID_EMAIL"}, status = 401)

