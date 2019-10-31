from django.urls import path

from . import views

#from account.views import (IndexView,ProfileView,UpdateProfile)
from account.views import ProfileView,UpdateProfile

from django.contrib.auth import views as my_views
app_name='account'

urlpatterns=[

#path('',IndexView.as_view(),name='index'),
path('',ProfileView.as_view(),name='profile'),

#path('<int:id>/make-deposit/',views.DepositView,name='DepositView'),

#path('<int:id>/withdraw-funds/',views.Withdraw,name='Withdraw-cash'),

path('update-profile-<int:pk>/',UpdateProfile.as_view(),name='update-view'),





]
