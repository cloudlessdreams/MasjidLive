from django.db import models

class MasjidArea(models.Model):
	# does this need an id for relation?
	city = models.CharField(max_length=100)


	def __str__(self):
		return self.city



class Masjid(models.Model):
	city = models.ForeignKey(MasjidArea, on_delete = models.CASCADE)
	name = models.CharField(max_length=100)
	fajr = models.TimeField()


	def __str__(self):
		return self.name


