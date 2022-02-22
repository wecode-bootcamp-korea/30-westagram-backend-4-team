import json
import bcrypt
import jwt
from django.views    import View
from django.http     import JsonResponse
from django.db.utils import IntegrityError
from .models         import User
from .validation     import validate_email, validate_password
from  westagram.settings  import SECRET_KEY

class SignUpView(View):
    def post(self,request):
        try:
            data         = json.loads(request.body)
            first_name   = data['first_name']
            second_name  = data['second_name']
            email        = data['email']
            password     = data['password']
            phone_number = data.get('phone_number','')
            
            if not validate_email(email):
                return JsonResponse({"message": "Invalid email form"}, status= 400)
            if not validate_password(password):
                return JsonResponse({"message": "Invalid password form"}, status= 400)
           
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode()

            User.objects.create(
                first_name   = first_name, 
                second_name  = second_name, 
                email        = email, 
                password     = hashed_password,
                phone_number = phone_number )   

            return JsonResponse({'message' : 'SUCCESS'}, status = 201)

        except IntegrityError:
            return JsonResponse({"message": "Email integrity error"}, status= 400)
       
        except KeyError:
            return JsonResponse({"message": "KEY ERROR"}, status= 400)

class LoginView(View):    
    def post(self,request):
        try:    
            data     = json.loads(request.body)
            new_email    = data['email']
            new_password = data['password']

            if not User.objects.filter(email = new_email).exists():
                return JsonResponse({"message" : "INVALID_UESR"}, status = 401)

            user=User.objects.get(email=new_email)

            if not bcrypt.checkpw(new_password.encode('utf-8'),user.password.encode('utf-8')):
                return JsonResponse({"message" : "INVALID_UESR"}, status = 401)

            access_token = jwt.encode({'id' : user.id}, SECRET_KEY, algorithm = 'HS256')
            return JsonResponse({'message': 'SUCCESS' ,'token':access_token }, status = 200)
    
        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status = 400)
            