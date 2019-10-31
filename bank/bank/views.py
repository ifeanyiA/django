from django.shortcuts import render
from django.views.generic.edit import CreateView
from account.models import Customer,Action
from account.forms import CustomUserCreationForm,CustomUserChangeForm
from django.urls import reverse_lazy
import secrets
from django.views.generic.base import TemplateView
from django.contrib.auth.views import  PasswordResetView

class SignUpView(CreateView):
	model=Customer
	form_class=CustomUserCreationForm
	template_name='signup.html'
	success_url=reverse_lazy('account:index')
	
class PasswordResetView(PasswordResetView):
	template_name='account/password_reset_form.html'
	success_url=reverse_lazy('/password_reset/done/')
	subject_template_name = 'account/password_reset_subject.txt'
	email_template_name = 'account/password_reset_email.html'
	

	
	
	
	
	


	
		
		


	
