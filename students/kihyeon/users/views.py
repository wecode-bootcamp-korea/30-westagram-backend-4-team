import json
import re

from django.http  import JsonResponse
from django.views import View

from users.models import User


class SignUpView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            
            EMAIL_VALIDATION    = r'^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
            PASSWORD_VALIDATION = r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[$@$!%*#?&])[A-Za-z\d$@$!%*#?&]{8,}$'
            email               = data['email']
            password            = data['password']
            phone_number        = data['phone_number'],

            if not re.match(EMAIL_VALIDATION, email):
                return JsonResponse({'Message' : 'Invalid Email'},       status = 400)
            
            if not re.match(PASSWORD_VALIDATION, password):
                return JsonResponse({'Message' : 'Invalid Password'},    status = 400)
            
            if User.objects.filter(email = email).exists():
                return JsonResponse({'Message' : 'Email Already Exist '}, status = 400)

            User.objects.create(
                first_name   = data["first_name"],
                last_name    = data["last_name"],
                email        = email,
                password     = password,
                phone_number = phone_number,
                created_at   = data["created_at"],
                updated_at   = data["updated_at"],
                
            )
            return JsonResponse({"MESSAGE": "User Created!"}, status=201)

        except KeyError:
            return JsonResponse({"MESSAGE": "KEY_ERROR"}, status=400)
