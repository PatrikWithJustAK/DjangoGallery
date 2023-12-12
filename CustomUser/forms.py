from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import User
class UserAuthenticationForm(AuthenticationForm):
    
    class Meta:
        model = User
        fields = ("email","password")


