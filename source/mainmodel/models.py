from django.db import models

# Create your models here.
class Klocal(models.Model):
  localname = models.CharField(max_length=200)
  owner = models.CharField(max_length=75)
  address = models.CharField(max_length=200)
  phone = models.CharField(max_length=30)
  email = models.EmailField(max_length=200)
  coords = models.CharField(max_length=100)
  cloth = models.TextField()

  def __unicode__(self):
      return self.localname
  

class Kcategory(models.Model):
  categoryname = models.CharField(max_length=200)
  
  def __unicode__(self):
    return self.categoryname


  
