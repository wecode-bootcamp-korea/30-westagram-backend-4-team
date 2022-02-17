from django.db import models

class User(models.Model):
	name = models.CharField(max_length=45)
	email = models.EmailField(max_length=254)
	password = models.CharField(max_length=40)
	phone = models.CharField(max_length=20)

	class Meta:
		db_table = 'users'

