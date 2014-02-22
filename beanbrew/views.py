from django.shortcuts import render
from beanbrew.models import Brew
from django.core.exceptions import ObjectDoesNotExist

def home(request):
    try:
        bean_brews = Brew.objects.all()
    except ObjectDoesNotExist:
        bean_brews = ()

    return render(request, "beanbrew/main.html", {
        'bean_brews': bean_brews,
    })
