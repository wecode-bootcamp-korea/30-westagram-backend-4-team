from django.db import models

# Create your models here.
class User(models.Model):
    first_name   = models.CharField(max_length=50)
    last_name    = models.CharField(max_length=50)
    email        = models.EmailField(max_length=50, unique=True)
    password     = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20, blank=True)
    created_at   = models.DateTimeField(auto_now_add=True)
    updated_at   = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = "users"
        

class Follow(models.Model):
    followuser = models.ForeignKey('User', related_name='followings', on_delete=models.CASCADE) 
    followeduser  =  models.ForeignKey('User', related_name='followed', on_delete=models.CASCADE) 
    
    class Meta:
        db_table = "follows"