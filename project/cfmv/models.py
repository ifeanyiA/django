from django.db import models

LANGUAGES=[
('php','Php'),
('django','Django'),
('laravel','Laravel'),

]

class DeveloperSkill(models.Model):
		file_app=models.CharField(max_length=30)
		
		def __str__(self):
				return self.file_app
				
				
				
				
class Person(models.Model):
		name=models.CharField(max_length=30)
		skills=models.ManyToManyField(DeveloperSkill)
		
		def __str__(self):
				return self.name

				
class Message(models.Model):
		message=models.CharField(max_length=100)
		
		def __str__(self):
				return self.message
				
