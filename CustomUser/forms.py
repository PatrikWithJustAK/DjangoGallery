from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import User
class UserAuthenticationForm(AuthenticationForm):
    
    class Meta:
        model = User
        fields = ("email","password")

        def clean(self):
            cleaned_data = super().clean() 
            email = cleaned_data.get("email")
            password = cleaned_data.get("password")



            return cleaned_data


