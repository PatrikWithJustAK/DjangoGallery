from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import UserAuthenticationForm
def mainpageview(request):
    return render(request, template_name="base.html")
def indexview(request):
    return render(request, template_name="index.html")
def loginview(request):
        if request.method == 'POST':
            form = UserAuthenticationForm(request, data=request.POST)
            if form.is_valid():
                email = form.cleaned_data.get('email')
                password = form.cleaned_data.get('password')
                user = authenticate(request, email=email, password=password)
                if user is not None:
                    login(request, user)
                    # Redirect to a success page.
                    return redirect('login')  # Replace 'home' with the name of your home page's URL
        else:
            form = UserAuthenticationForm()
            user = "dad"
        return render(request, 'login.html', {'form': form})
def signupview(request):
    return render(request, template_name="signup.html")