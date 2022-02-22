import json, bcrypt, jwt

from django.http  import JsonResponse
from django.views import View

from my_settings import ALGORITHM
from westagram.settings import SECRET_KEY

from users.models import User
from users.validations import validate_email, validate_password

class SignUpView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)

            username     = data['username']
            first_name   = data['first_name']
            last_name    = data['last_name']
            phone_number = data.get('phone_number', '')
            email        = data['email'] 
            password     = data['password']
            
            if not validate_email(email):
                return JsonResponse ({"message" : "INVALID_EMAIL"}, status=400)

            if not validate_password(password):
                return JsonResponse ({"message" : "INVALID_PASSWORD"}, status=400)
            
            if User.objects.filter(email = email).exists():
                return JsonResponse ({"message" : "EMAIL_OCCUPIED"}, status=409)
            
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
             
            User.objects.create(
                username     = username,
                first_name   = first_name,
                last_name    = last_name,
                phone_number = phone_number,
                email        = email,
                password     = hashed_password                
            )
            
            return JsonResponse({"message" : "SUCCESS"}, status=201)

        except KeyError:
            return JsonResponse({"message" : "KEY_ERROR"}, status=400)

class SignInView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            email    = data['email']
            password = data['password']
            user     = User.objects.get(email = email)

            if not bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
                return JsonResponse ({"message" : "INVALID_PASSWORD"}, status=401)

            access_token = jwt.encode({'id' : user.id}, SECRET_KEY, ALGORITHM)

            return JsonResponse({"access_token" : access_token, "message" : "SUCCESS"}, status=201)

        except KeyError:
            return JsonResponse({"message" : "KEY_ERROR"}, status=400)
  
        except User.DoesNotExist:
            return JsonResponse({"message" : "INVALID_USER: EMAIL DOES NOT EXIST"}, status=401)