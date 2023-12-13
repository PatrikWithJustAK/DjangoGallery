from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UserAuthenticationForm, CustomuserCreationForm
def mainpageview(request):
    return render(request, template_name="base.html")


def indexview(request):
    return render(request, template_name="index.html")


def loginview(request):
    if request.method == 'POST':
        form = UserAuthenticationForm(data=request.POST)
        if form.is_valid():
            # Form validation and user authentication logic
            email = form.cleaned_data.get("username")
            print(f"{email}")
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')  # Redirect to the index page after successful login
    else:
        form = UserAuthenticationForm()  # Initialize the form correctly for GET requests

    return render(request, 'login.html', {'form': form})

def logoutview(request):
    user = request.user
    if user is not None:
        logout(request)
        return redirect('index')
    else:
        return redirect('index') 



def signupview(request):
    if request.method == 'POST':
        form = CustomuserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            loginview(request,user)
            return redirect('index')
        else: 
            return redirect('signup')
    else:
        form = CustomuserCreationForm()
        context = {"form" : form}
        return render(request, "signup.html", context)