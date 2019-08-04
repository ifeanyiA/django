#from django import forms
#from .models import UserProfile,Article
#from django.forms import PasswordInput,TextInput,EmailInput

#class UserProfileForm(forms.Form):
		#fullname=forms.CharField(label="Full Name",widget=forms.TextInput)
		#email=forms.EmailField(label="Email",widget=forms.EmailInput)
		#password=forms.CharField(label="Password",widget=forms.PasswordInput)
		
		
		#def clean_name(self):
						#name=self.cleaned_data.get("fullname")
						#qs=UserProfile.objects.filter(fullname_iexact=fullname)
						#if qs.exist():
								#raise forms.ValidationError("name exist")
						#return fullname
		
		
		
		
#class UserProfileModelForm(forms.ModelForm):
		
		
		#class Meta:
				#model=UserProfile
				#fields=['fullname','email','password']
				#widgets={'password':PasswordInput, 'fullname':TextInput(attrs={'placeholder':'Enter full name'}),
				#'email':EmailInput(attrs={'placeholder':'Domain@example.com'}),}
				
				
				

#class ArticleModelForm(forms.ModelForm):
		#class Meta:
				#model=Article
				#fields=['title','article','pub_date']
				
				
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('email',)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email',)
