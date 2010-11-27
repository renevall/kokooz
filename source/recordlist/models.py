from django.db import models

# Create your models here.
class Table(models.Model):
	table = models.CharField(max_length=200)

class Element(models.Model):
	created = models.DateTimeField('creation date')
	element = models.CharField(max_length=300)
	link = models.CharField(max_length=200)
	description = models.CharField(max_length=500)
	table = models.ForeignKey(Table)
