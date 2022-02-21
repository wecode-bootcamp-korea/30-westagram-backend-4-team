import json
import re

from django.views    import View
from django.http     import JsonResponse
from django.db.utils import IntegrityError
from .models         import User
from .validation     import validate_email,validate_phone_number,validate_password

class SignUpView(View):
    def post(self,request):
        try:
            data         = json.loads(request.body)
            first_name   = data['first_name']
            second_name  = data['second_name']
            email        = data['email']
            password     = data['password']
            phone_number = data['phone_number']
            
            if not validate_email(email):
                return JsonResponse({"message": "Invalid email form"}, status= 400)
            if not validate_phone_number(phone_number):
                return JsonResponse({"message": "Invalid phone number form"}, status= 400)
            if not validate_password(password):
                return JsonResponse({"message": "Invalid password form"}, status= 400)

            User.objects.create(
                first_name=first_name, 
                second_name=second_name, 
                email=email, 
                password=password ,
                phone_number=phone_number)   

            return JsonResponse({'message' : 'SUCCESS'}, status = 201)

        except IntegrityError:
            return JsonResponse({"message": "Email integrity error"}, status= 400)
       
        except KeyError:
            return JsonResponse({"message": "KEY ERROR"}, status= 400)

class LoginView(View):    
    def get(self,request):
        try:    
            data     = json.loads(request.body)
            email    = data['email']
            password = data['password']
            if not User.objects.filter(email = email, password = password).exists():
                return JsonResponse({"message" : "INVALID_UESR"}, status = 401)
                
            return JsonResponse({'message': 'SUCCESS'}, status = 201)
    
        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status = 400)
            