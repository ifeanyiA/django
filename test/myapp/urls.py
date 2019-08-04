from django.urls import path

from . import views
from django.contrib.auth import views as myviews

urlpatterns=[
path('',views.index ,name='index'),

path('details/<int:id>/',views.details, name='details'),
path('<str:username>/',views.profile,name='profile'),
path('update/<int:id>/',views.update,name='update'),

]
