import json, bcrypt

from django.views import View
from django.http  import JsonResponse
from .models      import User
from .validations import check_email, check_password

class SignUpView(View):

    def post(self, request):
        try:
            data                     = json.loads(request.body)
            first_name               = data['first_name']
            last_name                = data['last_name']
            email                    = data['email']
            password                 = data['password']
            phone                    = data.get('phone', None)
            hashed_password          = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

            if check_email(email):
                return JsonResponse({"message" : "Check the email-form"}, status = 400)

            if check_password(password):
                return JsonResponse({"message" : "Check the password-form"}, status = 400)

            if User.objects.filter(email = email).exists():
                return JsonResponse({"message" : "Email arleady exist"}, status = 400)

            User.objects.create(
                        first_name = first_name,
                        last_name  = last_name,
                        email      = email,
                        password   = hashed_password,
                        phone      = phone
            )
            
            return JsonResponse({"message" : "SUCCESS"}, status = 201)

        except KeyError:
            return JsonResponse({"message" : "KEY_ERROR"}, status = 400)

class LogInView(View):

    def post(self,request):
        try:
            data           = json.loads(request.body)
            login_email    = data['email']
            login_password = data['password']
           
            if not User.objects.filter(email = login_email, password = login_password).exists():
                return JsonResponse({"message" : "INVALID_UESR"}, status = 401)

            return JsonResponse({"message" : "SUCCESS"}, status = 200)
            
        except KeyError:
            return JsonResponse({"message" : "KEY_ERROR"}, status = 400)
