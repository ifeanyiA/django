"""bank URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include,re_path
from django.views.generic.base import TemplateView
from django.contrib.auth import views
from . views import SignUpView
urlpatterns = [

   path('',TemplateView.as_view(template_name='home.html'),name='home'),
   
  #    path('loggedout/',TemplateView.as_view(template_name='chez.html'),name='chez'),
   
   
    
    path('accounts/', include('django.contrib.auth.urls')),
    
  #  path('logout/',views.LogoutView.as_view(next_page='chez',template_name='chez.html'),name='logout'), 
  
   #login views and the rest
  
   
path('login/',views.LoginView.as_view(template_name='login.html'),name='login'),


path('accounts/change-password/',views.PasswordChangeView.as_view(template_name='account/password_change.html',success_url='done/'),name='password_change'),

path('accounts/change-password/done/',views.PasswordChangeDoneView.as_view(template_name='account/password_change_done.html',extra_context={'confirm':'you have successfully changed'}),name='password_change_done'),








   
   path('signup/',SignUpView.as_view(),name='signup'),
   
path('admin/', admin.site.urls),
    path('account/',include('account.urls')),
 #   re_path(r'^(?:account-(?P<username>\d+)/)?$',include('account.urls'))
    
    
    
  
   
]
