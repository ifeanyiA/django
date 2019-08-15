from django import forms
from .models import Developer
from django.forms import CheckboxInput

LANGUAGES=[
('php','Php'),
('django','Django'),
('laravel','Laravel'),

]

class DeveloperForm(forms.Form):
		name=forms.CharField(label="Full Name")
		age=forms.CharField(widget=forms.NumberInput)
		php=forms.CharField(widget=forms.CheckboxInput)
		django=forms.CharField(widget=forms.CheckboxInput)
		laravel=forms.CharField(widget=forms.CheckboxInput)
		
		
		
class DeveloperModelForm(forms.ModelForm):
		
		class Meta:
				model=Developer
				fields=['name','age','php','django','laravel']
				widgets={'php':CheckboxInput(attrs={'name':'language'}),
				'django':CheckboxInput(attrs={'name':'language'}),
				
				'laravel':CheckboxInput(attrs={'name':'language'}),
				
				
				}
		
		
		
