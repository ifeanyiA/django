from django import forms
from .models import DeveloperSkill,Person,Message
from django.forms import CheckboxInput,TextInput

LANGUAGES=[
('php','Php'),
('django','Django'),
('laravel','Laravel'),

]

class DeveloperModelForm(forms.ModelForm):
		skills=forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple,
		queryset=DeveloperSkill.objects.all())
		
		class Meta:
				model=DeveloperSkill
				model=Person
				fields=['name','skills']
				
				widgets={'name':TextInput(attrs={"placeholder":"Enter full name"}),}
				

