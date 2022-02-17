from django.db import models

# Create your models here.
class UserInformation(models.Model):
    name         = models.CharField(max_length=50)
    email        = models.EmailField(max_length=50)
    password     = models.CharField(max_length=50, default=0)
    phone_number = models.IntegerField(max_length=15)
    
    class Meta:
        db_table = "userinfo"