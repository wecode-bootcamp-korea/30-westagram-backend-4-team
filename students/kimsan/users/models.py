from django.db import models


class User(models.Model):
    first_name        = models.CharField(max_length=20)
    second_name       = models.CharField(max_length=20)
    email             = models.CharField(max_length=100, unique=True)
    password          = models.CharField(max_length=255)
    phone_number      = models.CharField(max_length=20, blank=True, null=True)
    extra_information = models.TextField(blank=True, null=True)
    created_at        = models.DateTimeField(auto_now_add=True)
    updated_at        = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'users'


