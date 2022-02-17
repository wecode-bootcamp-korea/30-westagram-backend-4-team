from django.db import models

class User(models.Model):
    name      = models.CharField(max_length=45)
    email     = models.EmailField(max_length=254)
    password  = models.CharField(max_length=30)
    cellphone = models.CharField(max_length=15)


    class Meta:
        db_table = 'users'