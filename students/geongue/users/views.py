from django.views import View
from django.http  import JsonResponse
from .models      import *
import json
from .validation import *

# Create your views here.

class SignUpView(View):

    def post(self, request):
        data       = json.loads(request.body)
        first_name = data['first_name']
        last_name  = data['last_name']
        email      = data['email']
        password   = data['password']
        phone      = data['phone']

        try:
            if check_email(email):
                return JsonResponse({"message" : "Check the email-form"}, status = 400)

            if check_password(password):
                return JsonResponse({"message" : "Check the password-form"}, status = 400)

            if User.objects.filter(email = email).exists():
                return JsonResponse({"message" : "Email arleady exist"}, status = 400)

            User.objects.create(first_name = first_name, last_name = last_name, email = email,
                                 password = password, phone = phone)
            return JsonResponse({"message" : "SUCCESS"}, status = 201)

        except KeyError:
            return JsonResponse({"message" : "KEY_ERROR"}, status = 400)