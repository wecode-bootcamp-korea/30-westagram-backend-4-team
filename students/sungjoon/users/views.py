import json
import re

from django.http  import JsonResponse
from django.views import View

from users.models import User

class UserView(View):
    def post(self, request):
        data = json.loads(request.body)

        email_regex    = re.match('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9_-]+\.[a-zA-Z0-9.]+$', data['email'])
        password_regex = re.match('^(?=.*[a-zA-Z])(?=.*[!@#$%^*+=-])(?=.*[0-9]){8,}$', data['password'])

        try:
            if not email_regex or password_regex:
                return JsonResponse ({"message" : "FORBIDDEN"}, status=403)
            
            if User.objects.filter(email = data['email']).exists():
                return JsonResponse ({"message" : "CONFLICT"}, status=409)
            
            User.objects.create(
                username     = data['username'],
                password     = data['password'],
                first_name   = data['first_name'],
                last_name    = data['last_name'],
                email        = data['email'],
                phone_number = data['phone_number']
            )
            
            return JsonResponse({"message" : "SUCCESS"}, status=201)

        except KeyError:
            return JsonResponse({"message" : "KEY_ERROR"}, status=400)