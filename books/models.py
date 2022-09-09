from django.db import models

# Create your models here.


class Book(models.Model):
	title = models.CharField(max_length=80)
	subtitle = models.CharField(max_length=60)
	author = models.CharField(max_length=70)
	isbn = models.CharField(max_length=10)

	def __str__(self):
		return self.title
