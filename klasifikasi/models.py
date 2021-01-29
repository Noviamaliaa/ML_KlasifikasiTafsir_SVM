from django.db import models

# Create your models here.
class Data(models.Model):
	Data = models.FileField(upload_to='media/')
	def __str__(self):
		return self.Data