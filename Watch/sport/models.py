#from django.db import models







#class UserProfile(models.Model):
		#fullname=models.CharField(verbose_name="Full Name",max_length=50)
		#email=models.EmailField(verbose_name="Email Address",unique=True)
		#password=models.CharField(verbose_name="Password",max_length=20)
		
		
		#def __str__(self):
		    #fullname=" %(id)s %(fullname)s"
		    #return fullname % {'id':self.id,'fullname':self.fullname}
	
	
   
			
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from .managers import CustomUserManager
from django.conf import settings

class CustomUser(AbstractBaseUser, PermissionsMixin):
		
    email = models.EmailField(_('email address'), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
        
        
 
	
class Article(models.Model):
		
		fullname=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,verbose_name="Full Name")
		title=models.CharField(verbose_name="Title",max_length=50)
		article=models.TextField(verbose_name="Aricle")
		pub_date=models.DateField(verbose_name="Date")
		
		def __str__(self):
				return self.title
      
