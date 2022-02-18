import re

def validate_email(email):
    if re.match('^[a-zA-Z0-9-+_.]+@[a-zA-Z0-9-+_]+\.[a-zA-Z0-9-+_.]+$',email)==None:
        return False
    else:
        return True

def validate_phone_number(phone_number):
    if re.match('[0-9]{3}-[0-9]{4}-[0-9]{4}$',phone_number)==None:
        return False
    else:
        return True

def validate_password(password):
    if re.match('[\W\w]{8}[\W\w]+',password)==None:
        return False
    else:
        return True