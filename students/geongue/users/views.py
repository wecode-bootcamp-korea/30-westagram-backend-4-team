from django.views import View
from django.http import JsonResponse
from .models import *
import json
import re

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
            email_check = re.compile("^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")

            if (email_check.match(data["email"]) != None) == False:
                return JsonResponse({"message" : "Check the email-form"}, status = 400)
            elif len(password) < 8 or re.search("[a-za]+" ,password) is None or re.search("[0-9]+",
                 password) is None or re.search("[`~!@#$%^&*(),<.>/?]+", password) is None :
                return JsonResponse({"message" : "Check the password-form"}, status = 400)
            elif User.objects.filter(email = email).exists():
                return JsonResponse({"message" : "Email arleady exist"}, status = 400)

            User.objects.create(first_name = first_name, last_name = last_name, email = email,
                                 password = password, phone = phone)
            return JsonResponse({"message" : "SUCCESS"}, status = 201)

        except KeyError:
            return JsonResponse({"message" : "KEY_ERROR"}, status = 400)

        # data        = json.loads(request.body)
        # email_check = re.compile("^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")

        # if data["email"] == None or data["password"] == None :
        #     return JsonResponse({"message" : "KEY_ERROR"}, status = 400)
        # elif (email_check.match(data["email"]) != None) == False:
        #     return JsonResponse({"message" : "Check the email-form"}, status = 400)
        # elif len(data["password"]) < 8 or re.search("[a-za]+" ,data["password"]) is None or re.search("[0-9]+",
        #          data["password"]) is None or re.search("[`~!@#$%^&*(),<.>/?]+", data["password"]) is None :
        #     return JsonResponse({"message" : "Check the password-form"}, status = 400)
        # elif data["email"] == User.object.get(email = data["email"]) :
        #     return JsonResponse({"message" : "Check the email-form"}, status = 400)
        # else:
        #     User.objects.create(first_name = data["first_name"], last_name = data["last_name"], email=data["email"],
        #                     password=data["password"], phone=data["phone"], create_at=datetime.time())
        #     return JsonResponse({"mesaage" : "SUCCESS"}, status = 200)

