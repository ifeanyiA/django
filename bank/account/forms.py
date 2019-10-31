from django import forms
import secrets
from django.contrib.auth.forms import  UserCreationForm,UserChangeForm
from .models import Customer,Action
from django.forms import TextInput,NumberInput
from django.utils.translation import gettext_lazy as _
from django.urls import reverse

class CustomUserCreationForm(UserCreationForm):
	class Meta(UserCreationForm):
		model=Customer
		fields=('username','first_name','middle_name','last_name','email','phone')
		
		widgets={'username':TextInput(attrs={'placeholder':'Username'}),
		
			}
			
		help_texts={
		'username':_(''),
		
		}
		
			

class CustomUserChangeForm(UserChangeForm):
	class Meta(UserChangeForm):
		model=Customer
		fields=('username','first_name','middle_name','last_name','email','phone')
		
		
class UpdateForm(forms.ModelForm):
	class Meta:
		model=Customer
		fields=['balance']
		widgets={'balance':NumberInput(attrs={'placeholder':'Enter Amount','value':'Enter Amount'}),
		}
		labels={'balance':('Enter Amount'),}
		
		
	
		
				

			
		