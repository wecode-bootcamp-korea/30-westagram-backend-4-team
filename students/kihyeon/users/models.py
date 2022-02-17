from django.db import models

# Create your models here.
class User(models.Model):
    first_name   = models.CharField(max_length=50)
    last_name    = models.CharField(max_length=50, null=True)
    email        = models.EmailField(max_length=50, unique=True)
    password     = models.CharField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=15)
    created_at   = models.DateTimeField(auto_now_add=True, null=True)
    updated_at   = models.DateTimeField(auto_now=True, null=True)
    
    class Meta:
        db_table = "members"