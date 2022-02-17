from django.db import models


class User(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    phone_number=models.IntegerField()

    class Meta:
        db_table = 'owners'


