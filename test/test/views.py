from django.urls import reverse_lazy
from django.shortcuts import render,get_object_or_404
from django.views.generic.edit import CreateView
from myapp.models import CustomUser,Article
from myapp.forms import CustomUserCreationForm

class SignUpView(CreateView):
		
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
    
