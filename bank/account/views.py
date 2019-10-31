from django.shortcuts import render,get_object_or_404
from .models import Customer,Action
from .forms import UpdateForm
from django.utils.decorators import method_decorator
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.views.generic.edit  import UpdateView
from django.urls import reverse_lazy,reverse
from django.conf import settings
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.utils import timezone


decorators=[login_required]


# Create your views here.
#@method_decorator(decorators,name='dispatch')
#class IndexView(generic.ListView):
	#model=Customer

#	template_name='account/index.html'
#	context_object_name='customer'
	
#	def get_context_data(self,**kwargs):
#		context=super().get_context_data(**kwargs)
#		context['action']=Action.objects.all()
#		return context
	
	
		
@method_decorator(decorators,name='dispatch')
class ProfileView(generic.ListView):
	model=Customer
	template_name='account/profile.html'
	context_object_name='profile'
	
	
		

	
			
@method_decorator(decorators,name='dispatch')	

class UpdateProfile(UpdateView):
	model=Customer
	template_name='account/update.html'
	fields=['first_name','middle_name','last_name','phone']
#	success_url='/account/profile/{id}'




	

@login_required
def DepositView(request,id):
	if request.method=='POST':
		form=UpdateForm(request.POST or None)
		if form.is_valid():
			currentUser=get_object_or_404(Customer,pk=id)
			data=form.cleaned_data['balance']
			
			currentUser.balance+=data
			
			currentUser.save()
			if data<1:
				currentUser.save()
				
			
			else:
				
				msg='Deposit:+€{}'.format(data)
				activity=currentUser.action_set.create(action=msg,pub_date=timezone.now())
				activity.save()
			#pass
			return HttpResponseRedirect(reverse('account:index'))
	form=UpdateForm()
	template='account/deposit.html'
	return render(request,template,{'form':form})
			
    

@login_required
def Withdraw(request,id):
	if request.method=='POST':
		form=UpdateForm(request.POST or None)
		if form.is_valid():
			currentUser=get_object_or_404(Customer,pk=id)
			data=form.cleaned_data['balance']
			amount=currentUser.balance
			if data>amount:
				template='account/error.html'
				return render(request,template,{'data':data})
				
			
			currentUser.balance-=data
			currentUser.save()
			if data<1:
				currentUser.save()
			else:
				
				msg='Withdrawal:-€{}'.format(data)
				activity=currentUser.action_set.create(action=msg,pub_date=timezone.now())
				activity.save()
			
			#pass
			return HttpResponseRedirect(reverse('account:index'))
	form=UpdateForm()
	template='account/withdraw.html'
	return render(request,template,{'form':form})
			
    

		
	
 
	
	

