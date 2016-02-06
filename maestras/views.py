from django.shortcuts import render

# Create your views here.
class Country(models.Model):
	name = model.ChartField(max_lenght=50)
	iso = model.ChartField(max_lenght=4)

	def __str__(self):
		return name

	class Meta:
			verbose_name_plural = "Countries"