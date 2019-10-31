from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings



from django.urls import reverse
# Create your models here.
class Customer(AbstractUser):
	pass
	middle_name=models.CharField(verbose_name='Middle Name',max_length=20)

	phone=models.IntegerField(verbose_name='Phone Number',default=0)

	email=models.EmailField(unique=True)
	balance=models.FloatField(verbose_name='Account Balance',max_length=130,default=0.00)


	
	USERNAME_FIELD='email'
	REQUIRED_FIELDS=['username']
	
	
	
	def get_absolute_url(self):
		#return reverse('account:profile',kwargs={'pk':self.pk})
		
		
		return reverse('account:profile')
		
	
	
	def __str__(self):
		return self.first_name


class Action(models.Model):
	user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
	action=models.CharField(max_length=100,verbose_name='Activities')
	pub_date=models.DateTimeField()
	
	
	def __str__(self):
		return  self.action
		
		



