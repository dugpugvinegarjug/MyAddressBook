from django.db import models

class Address(models.Model):
	name = models.CharField(max_length=200)
	email = models.EmailField(max_length=200)
	phone = models.CharField(max_length=15)
	address = models.CharField(max_length=200)
	city = models.CharField(max_length=200)
	stateID = models.CharField(max_length=200)
	countryID = models.CharField(max_length=200)
	zipcode = models.CharField(max_length=10)
	age = models.IntegerField(default=0)

	def __str__(self):
		return self.name