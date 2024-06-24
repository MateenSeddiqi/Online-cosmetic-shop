from django.db import models

# Create your models here.
class Feedback(models.Model):
	name = models.CharField(max_length=100, null=True, blank=True)
	email =  models.CharField(max_length=100, null=True, blank=True)
	feedback = models.TextField(null=True, blank=True)

	def __str__(self):
		return(f"{self.name} {self.email}")
	
class Product(models.Model):
	name = models.CharField(max_length=100, null=True, blank=True)
	company = models.CharField(max_length=200, null=True, blank=True)
	cost = models.CharField(max_length=100, null=True, blank=True)
	image = models.ImageField(upload_to="products/images", null=True, blank=True)