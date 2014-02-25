from django.shortcuts import render
from django.http import HttpResponseRedirect
from beanbrew.models import Brew
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic.base import View
from beanbrew.forms import BrewCreationForm
from bean.models import Bean


def home(request):
    try:
        bean_brews = Brew.objects.all()
    except ObjectDoesNotExist:
        bean_brews = ()

    return render(request, "beanbrew/main.html", {
        'bean_brews': bean_brews,
    })


class BrewView(View):
    template_name = 'beanbrew/add_brew.html'

    def get(self, request):
        form = BrewCreationForm()
        try:
            beans = Bean.objects.all()
        except Bean.DoesNotExist:
            beans = ()
        return render(request, self.template_name, {
            "form": form,
            "beans": beans,
        })

    def post(self, request):
        form = BrewCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/beanbrew/')
