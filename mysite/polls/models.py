
from django.db import models
import datetime
from django.utils import timezone

# Create your models here.



class Question(models.Model):
    
    
    # models field 
    question_text=models.CharField(max_length=200)
    pub_date=models.DateTimeField('date published')
    # for display
    def __str__(self):
        result ="%(id)s  %(question)s  %(date)s" 
        return result % {"id":self.id,"question":self.question_text,"date":self.pub_date}
        
    def was_published_recently(self):
        return self.pub_date>= timezone.now()-datetime.timedelta(days=1)

class Choice(models.Model):
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text=models.CharField(max_length=200)
    votes=models.IntegerField(default=0)
    # for display
    def __str__(self):
        result="%(id)s  %(choice)s " 
        return result % { "id": self.id,"choice":self.choice_text,}