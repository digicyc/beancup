from django.shortcuts import render_to_response, redirect, render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from beancup.forms import BeanUserCreationForm


def home(request):
    user = request.user

    if request.user.is_authenticated():
        act_user = user.first_name
    else:
        act_user = 'Anonymous'

    return render_to_response('main.html', {
        'act_user': act_user,
        'user': user,
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
    return redirect("/")


def profile(request):
    return render(request, "auth/profile.html")


def bean_register(request):
    if request.method == 'POST':
        form = BeanUserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/")

    else:
        form = BeanUserCreationForm()
    return render(request, "auth/registration.html", {
        'form': form,
    })