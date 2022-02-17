from django.db import models


class User(models.Model):
    first_name  = models.CharField(max_length=20, blank=True, null=True)
    second_name = models.CharField(max_length=20, blank=True, null=True)
    email       = models.CharField(max_length=100, blank=True, null=True)
    password    = models.CharField(max_length=50, blank=True, null=True)
    phone_number=models.IntegerField( blank=True, null=True)
    extra_info  =models.TextField( blank=True, null=True)
    class Meta:
        db_table = 'users'


