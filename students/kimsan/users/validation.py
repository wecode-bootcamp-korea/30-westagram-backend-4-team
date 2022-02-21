import re

def validate_email(email):
    return re.match('^[a-zA-Z0-9-+_.]+@[a-zA-Z0-9-+_]+\.[a-zA-Z0-9-+_.]+$',email)
    
def validate_phone_number(phone_number):
    return re.match('[0-9]{3}-[0-9]{4}-[0-9]{4}$',phone_number)

def validate_password(password):
    return re.match('^(?=.*[A-Za-z])(?=.*\d)(?=.*[$@$!%*#?&])[A-Za-z\d$@$!%*#?&]{8,}$',password)
