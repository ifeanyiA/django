from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse
from .models import Developer
from .forms import DeveloperModelForm

# Create your views here.
def index(request):
		template="cfmv/index.html"
		time=timezone.now()
		context={'time':time}
		return render(request,template,context)
		
		
def myform(request):
		form=DeveloperModelForm(request.POST or None)
		if form.is_valid():
				form.save()
				message="successfully registered"
				return render(request,"cfmv/success.html",{'message':message})
		template="cfmv/form.html"
		time=timezone.now()
		form=DeveloperModelForm()
		context={'time':time,'form':form}
		return render(request,template,context)
		
