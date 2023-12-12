from django.shortcuts import render
from django.views.generic import TemplateView 
# Create your views here.
def mainpageview(request):
    return render(request, template_name="base.html")
def indexview(request):
    return render(request, template_name="index.html")
def loginview(request):
    return render(request, template_name="login.html")
def signupview(request):
    return render(request, template_name="signup.html")