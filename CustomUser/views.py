from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import UserAuthenticationForm
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
def signupview(request):
    return render(request, template_name="signup.html")