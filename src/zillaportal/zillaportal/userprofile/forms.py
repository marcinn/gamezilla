# -*- coding: utf-8 -*

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

import settings

class UploadAvatar(forms.Form):
    avatar_img = forms.ImageField("Zmień avatar")
    
    def clean_avatar_img (self):
		pass


class RegisterForm(UserCreationForm):
	email = forms.EmailField(label = "Email")
	first_name = forms.CharField(label = "First name")
	last_name = forms.CharField(label = "Last name")
	avatar = forms.ImageField()

#	def __init__(self, *args, **kwargs):
#		super(RegisterForm).__init__(*args, **kwargs)
	
	def save(self, commit=True):
		user = super(RegisterForm, self).save(commit=False)
		first_name = self.cleaned_data["first_name"].split()
		last_name = self.cleaned_data["last_name"].split()
		user.first_name = first_name
		user.last_name = last_name
		user.email = self.cleaned_data["email"]
		avatar = self.cleaned_data["avatar"]
		if commit:
			user.save()
		return user

