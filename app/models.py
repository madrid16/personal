#encoding:utf-8
from django.db import models

class contact(models.Model):
	con_name = models.CharField(max_length=200)
	con_number = models.CharField(max_length=10)
	con_email = models.CharField(max_length=200)
	con_subject = models.CharField(max_length=200)
	con_message = models.TextField(max_length=300)
	con_date = models.DateTimeField(auto_now=True)
	
	def __unicode__(self):
		return self.con_name
		
