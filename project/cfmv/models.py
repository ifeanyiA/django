from django.db import models

class Developer(models.Model):
		name=models.CharField(verbose_name="Full Name",max_length=30)
		age=models.IntegerField(default=0)
		php=models.BooleanField(verbose_name="Php",default=False)
		django=models.BooleanField(verbose_name="Django",default=False)
		laravel=models.BooleanField(verbose_name="Laravel",default=False)
		
		def __str__(self):
				return self.name
