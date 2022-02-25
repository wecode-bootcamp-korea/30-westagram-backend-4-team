import json, bcrypt, jwt

from django.http  import JsonResponse
from django.views import View

from users.models     import User, Follow
from users.validators import validate_email, validate_password
from secret           import ALGORITHM
from config.settings  import SECRET_KEY


def login_decorator(func):
    def wrapper(self, request, *args, **kwargs):
        try:
            if not 'Authorization' in request.headers:
                return JsonResponse({"message" : "No Authorization in headers"})
            
            access_token   = request.headers.get("Authorization")
            payload = jwt.decode(access_token, SECRET_KEY, ALGORITHM)
            user_id = payload['user_id']

            if not User.objects.filter(id = user_id).exists():
                return JsonResponse({"message" : "INVALID_UESR"}, status = 401)
            
            user         = User.objects.get(id = user_id)
            request.user = user
            
            return func(self, request, *args, **kwargs)

        except jwt.exceptions.DecodeError as e:
            return JsonResponse({"message" : "INVALID_TOKEN"}, status = 400)

        except KeyError:
            return JsonResponse({"message" : "DECORATOR_KEYERROR"}, status = 400)
    return wrapper             
