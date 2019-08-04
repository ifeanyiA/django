from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.shortcuts import get_object_or_404,render
from polls.models import Choice,Question
from django.utils import timezone
from datetime import date,time
import datetime
from django.urls import reverse


# Create your views here.

    
    
def index(request):
    Today_date=datetime.datetime.now().date()
    Today_time=datetime.datetime.now().time()
   
    birthday=datetime.date(2019,4,26)
    #if birthday>date.today():
    if date.today()==birthday:      
        wish="Happy birthday! %(name)s " % {"name":"Ifeanyi Emmanuel Anaga"}
    else:
        wish="Belated "
    
   
    latest_question_list=Question.objects.order_by('-pub_date')[:6]
    
    context={'wish':wish,'latest_question_list':latest_question_list,'Today_date':Today_date,'Today_time':Today_time,}
    
    return render(request,'polls/index.html',context)
    
    
      
def details(request,question_id):
    Today_date=datetime.datetime.now().date()
    Today_time=datetime.datetime.now().time()
    
    
    question=get_object_or_404(Question,pk=question_id)
    choices=question.choice_set.all()
       
    return render(request,'polls/details.html',{'choices':choices,'question':question,'Today_date':Today_date,'Today_time':Today_time})
   
   
   
   
def results(request,question_id):
    question=get_object_or_404(Question,pk=question_id)
    return render(request,'polls/results.html',{'question':question})
    
def vote(request,question_id):
    question=get_object_or_404(Question,pk=question_id)
    try:
        selected_choice=question.choice_set.get(pk=request.POST['choice'])
    except (KeyError,Choice.DoesNotExist):
        #redisplaying question voting form
        return render(request,'polls/details.html',{'question':question,'error_message':"you didn't select a choice"})
    else:
        
        selected_choice.votes=selected_choice.votes +1
        selected_choice.save()
        
      #  selected_choice.votes=+1
        
        
        # returning result polls/question.id/results
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
           
  
  

     