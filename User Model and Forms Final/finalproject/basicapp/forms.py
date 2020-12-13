from basicapp.models import UserProfileInfo
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm

from django.core import validators

class UserForm(ModelForm):
    #Custom validator
	def check_if_z(value):
		if value[0].lower != 'z':
			raise forms.ValidationError('Needs to start with z')


	username = forms.CharField(validators = [check_if_z])
	#Hashing the password

	password = forms.CharField(widget = forms.PasswordInput())
	class Meta():
		model = User
		fields = ('username', 'email', 'password')
		widgets = {'hiddenUser': forms.HiddenInput()}

class UserProfileInfoForm(ModelForm):
	class Meta():
		model = UserProfileInfo
		fields = ('portfolio_site', 'profile_pic')
		widgets = {'hiddenUserProfileForm': forms.HiddenInput()}

