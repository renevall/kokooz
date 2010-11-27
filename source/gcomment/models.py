from django.db import models
from table.models import Table
from django import forms

# Create your models here.
class Comment(models.Model):
	comment=models.CharField(max_length=500)
	created=models.DateTimeField('creation date')
	table = models.ForeignKey(Table)	

class CommentForm(forms.Form):
	comment = forms.CharField(max_length=500,widget=forms.Textarea)
	table_id = forms.CharField()
