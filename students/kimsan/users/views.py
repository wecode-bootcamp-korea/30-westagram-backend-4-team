import json

from django.views import View
from django.http import JsonResponse
from django.db.utils import IntegrityError
from .models import User
import re

#test set
# valid input1  http -v POST 127.0.0.1:8080/users/sign_up first_name='김' second_name='산' email='itzmi+san@naver.com' password="azAZn123" phone_number='010-1234-5678'
#valid input2  http -v POST 127.0.0.1:8080/users/sign_up first_name='김' second_name='산' email='itzmi+gun@naver.com' password="azAZ_2d@n123!" phone_number='010-1234-5678'
# invalid input http -v POST 127.0.0.1:8080/users/sign_up first_name='김' second_name='산' email='email4n@naver.com' password="azA__++--3" phone_number='010-1234-5678'

class UserView(View):
    def post(self,request):
        try:
            data         = json.loads(request.body)
            first_name   = data['first_name']
            second_name  = data['second_name']
            email        = data['email']
            password     = data['password']
            phone_number = data['phone_number']
            
            regex_email        = re.compile('^[a-zA-Z0-9-+_.]+@[a-zA-Z0-9-+_]+\.[a-zA-Z0-9-+_.]+$')
            regex_phone_number = re.compile('[0-9]{3}-[0-9]{4}-[0-9]{4}$')
            regex_password     = re.compile('[\W\w]{8}[\W\w]+')

            #email,phone_number,password의 validation 검사
            if regex_email.match(email)==None:
                return JsonResponse({"message": "Invalid email form"}, status= 400)
            if regex_phone_number.match(phone_number)==None:
                return JsonResponse({"message": "Invalid phone number form"}, status= 400)
            if regex_password.match(password)==None:
                return JsonResponse({"message": "Invalid password form"}, status= 400)

            #database에 저장
            User.objects.create(first_name=first_name, second_name=second_name, email=email, password=password ,phone_number=phone_number)   
            return JsonResponse({'message' : 'SUCCESS'}, status = 201)

        #만약 이미 database에 있는 email일 경우
        except IntegrityError as e:
            return JsonResponse({"message": "Email integrity error"}, status= 400)
       
