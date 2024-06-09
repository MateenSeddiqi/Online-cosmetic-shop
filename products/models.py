from django.db import models

# Create your models here.
class Feedback(models.Model):
	name = models.CharField(max_length=50)
	email =  models.CharField(max_length=100)
	feedback = models.TextField()

	def __str__(self):
		return(f"{self.name} {self.email}")