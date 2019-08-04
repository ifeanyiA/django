from django.urls import reverse_lazy
from django.shortcuts import render,get_object_or_404
from django.views.generic.edit import CreateView
from .models import CustomUser,Article
from .forms import CustomUserCreationForm,UpdateCustomUser
from django.contrib.auth.decorators import login_required




#class SignUpView(CreateView):
		
   # form_class = CustomUserCreationForm
   # success_url = reverse_lazy('login')
   # template_name = 'signup.html'
    
@login_required
def index(request):
		title=Article.objects.all()
		
		template="myapp/login.html"
		context={'title':title}
		return render(request,template,context)
		
@login_required  
def details(request,id):
		details=get_object_or_404(Article,pk=id)
		author=details.author
		template="myapp/detail.html"
		return render(request,template,{'details':details,'author':author})
		
@login_required 
def profile(request,username):
		
		profile=get_object_or_404(CustomUser,username=username)
		template="myapp/profile.html"
		return render(request,template,{'profile':profile})
		
		
		
def update(request,id):
		obj=get_object_or_404(CustomUser,pk=id)
		form=UpdateCustomUser(request.POST or None,instance=obj)
		if form.is_valid:
				m=form.save(commit=False)
				
				m.save()
				
		template="myapp/update.html"
		return render(request,template,{'form':form})
