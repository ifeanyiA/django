from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class CustomUser(AbstractUser):
		pass
		
		
		firstname=models.CharField(max_length=40,verbose_name="First Name")
		lastname=models.CharField(max_length=40,verbose_name="Last Name")
		phone=models.CharField(max_length=20,verbose_name="Phone Number")
		
		def __str__(self):
				result= "%(firstname)s %(lastname)s"
				return result % {'firstname':self.firstname,'lastname':self.lastname,}

class Article(models.Model):
		author=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
		title=models.CharField(verbose_name="Title",max_length=30)
		slug=models.SlugField(unique=True)
		article=models.TextField()
		pub_date=models.DateField(verbose_name="Publication Date")
		
		def __str__(self):
				return self.title
