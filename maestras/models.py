from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Country(models.Model):
	name = models.CharField(max_length=50)
	iso = models.CharField(max_length=4)

	def __str__(self):
		return self.name

	class Meta:
			verbose_name_plural = "Countries"