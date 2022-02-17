from django.db import models

class User(models.Model):
    username     = models.CharField(max_length=50)
    first_name   = models.CharField(max_length=45)
    last_name    = models.CharField(max_length=45)
    email        = models.EmailField(max_length=254, unique=True)
    password     = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=30)
    created_at   = models.DateTimeField(auto_now_add=True)
    updated_at   = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'users'