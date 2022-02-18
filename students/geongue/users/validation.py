import re

EMAIL_CHECK = re.compile("^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
PASSWORD_CHECK = re.compile("^(?=.*\d)(?=.*[a-zA-Z])[0-9a-zA-Z!@#$%^&*]{8,}")

def check_email(email):
     if EMAIL_CHECK.match(email) == None :
        return True
 
def check_password(password):
     if PASSWORD_CHECK.match(password) == None:
        return True
    