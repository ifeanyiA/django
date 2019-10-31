from django.contrib import admin
from .models import Customer,Action
from django.contrib.auth import  get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm,CustomUserChangeForm

class CustomUserAdmin(UserAdmin):
	add_form=CustomUserCreationForm
	form=CustomUserChangeForm
	model=Customer
	list_display=['username','email']

admin.site.register(Customer,CustomUserAdmin);
admin.site.register(Action)

