import settings
from django import forms

class UploadAvatar(forms.Form):
    avatar_img = forms.ImageField("Zmień avatar")
    
    def clean_avatar_img (self):
		pass
