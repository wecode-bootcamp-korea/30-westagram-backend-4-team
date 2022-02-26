import json, bcrypt, jwt

from django.views       import View
from django.http        import JsonResponse
from .models            import User
from .validations       import check_email, check_password
from westagram.settings import SECRET_KEY, ALGORITHM

class SignUpView(View):

    def post(self, request):
        try:
            data                     = json.loads(request.body)
            first_name               = data['first_name']
            last_name                = data['last_name']
            email                    = data['email']
            password                 = data['password']
            phone                    = data.get('phone', '')
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

            if not User.objects.filter(email = login_email).exists():
                return JsonResponse({"message" : "INVALID_UESR"}, status = 401)

            user         = User.objects.get(email = login_email)
            access_token = jwt.encode({'user_id' : user.id}, SECRET_KEY, algorithm = ALGORITHM)
            print(type(access_token))
            
            if not bcrypt.checkpw(login_password.encode('utf-8'), user.password.encode('utf-8')):
                return JsonResponse({"message" : "Wrong password"}, status = 401)

            return JsonResponse({"message" : "SUCCESS", "token" : access_token}, status = 200)
            
        except KeyError:
            return JsonResponse({"message" : "KEY_ERROR"}, status = 400)