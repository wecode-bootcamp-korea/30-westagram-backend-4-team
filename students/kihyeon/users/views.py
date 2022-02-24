import json, bcrypt, jwt

from django.http  import JsonResponse
from django.views import View

from users.models     import User, Follow
from users.validators import validate_email, validate_password
from secret           import ALGORITHM
from config.settings  import SECRET_KEY

class SignUpView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)

            email        = data['email']
            password     = data.get('password', 'password@123')
            phone_number = data.get('phone_number', '')
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

            if not validate_email(email):
                return JsonResponse({'Message' : 'Invalid Email'}, status = 400)
            
            if not validate_password(password):
                return JsonResponse({'Message' : 'Invalid Password'}, status = 400)
            
            if User.objects.filter(email = email).exists():
                return JsonResponse({'Message' : 'Email Already Exists'}, status = 400)

            User.objects.create(
                first_name   = data.get("first_name", ""),
                last_name    = data.get("last_name",""),
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

            access_token = jwt.encode({'user_id' : user.id}, SECRET_KEY, ALGORITHM)
            return JsonResponse({"message" : "LOGIN_SUCCESS!", "token" : access_token}, status = 201)
            
        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)
        
        except User.DoesNotExist:
            return JsonResponse({"message" : "INVALID_EMAIL"}, status = 401)

class FollowView(View):
    def post(self, request):
        try:
            data    = json.loads(request.body)
            payload = jwt.decode(data["token"], SECRET_KEY, ALGORITHM)
            followed_user = data['followed_user'] 
            following_user = payload['following_user'] 
            
            get_follow = Follow.objects.get(following_user_id = following_user)
            get_folloed = Follow.objects.get(following_user_id = following_user)

            if get_follow.id == get_folloed.id:
                get_follow.delete()
                return JsonResponse({"message" : "DELETED_FOLLOWING"}, status = 201)
            
            if followed_user == '' or following_user == '':
                return JsonResponse({"message" : "Please Type User ID"}, status = 400)
            
            Follow.objects.create(
                following_user = User.objects.get(id=following_user),
                followed_user = User.objects.get(id=followed_user),
            )
            return JsonResponse({"message" : "SUCCESS"}, status = 201)

        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)
        