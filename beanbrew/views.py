from django.shortcuts import render
from beanbrew.models import BeanBrew
from django.core.exceptions import ObjectDoesNotExist

def home(request):
    try:
        bean_brews = BeanBrew.objects.get()
    except ObjectDoesNotExist:
        bean_brews = ()

    return render(request, "beanbrew/main.html", {
        'bean_brews': bean_brews,
    })
