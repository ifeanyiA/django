from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import CustomUser
from django.forms import NumberInput







class CustomUserCreationForm(UserCreationForm):
		class Meta(UserCreationForm):
				model=CustomUser
				fields=('firstname','lastname','username','phone','email',)
				widgets={'phone':NumberInput}
				
class CustomUserChangeForm(UserChangeForm):
		class Meta(UserChangeForm):
				model=CustomUser
				fields=('firstname','lastname','username','phone','email',)
				widgets={'phone':NumberInput}
				
				
				
class UpdateCustomUser(forms.ModelForm):
		class Meta:
				model=CustomUser
				fields=['firstname','lastname','username','phone','email']
				widgets={'phone':NumberInput}
				
			


		
