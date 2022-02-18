import re

def verify_email(email):
    EMAIL_REGEX = '^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9_-]+\.[a-zA-Z0-9.]+$'
    return re.match(EMAIL_REGEX, email)

def verify_password(password):
    PASSWORD_REGEX = '^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$'
    return re.match(PASSWORD_REGEX, password)
