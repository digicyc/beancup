from django.shortcuts import render_to_response, redirect, render
from django.contrib.auth import authenticate, login, logout


def home(request):
    return render_to_response('main.html', {
        'greeting': 'Welcome!'
    })

def bean_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect("/")
            else:
                return redirect("/login")
        else:
            return render(request, 'auth/login.html')

    return render(request, 'auth/login.html')

def bean_logout(request):
    logout(request)