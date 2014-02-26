from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponseRedirect
from bean.forms import BeanCreationForm


class BeanView(View):
    template_name = 'bean/add_bean.html'
    form = BeanCreationForm()

    def get(self, request):
        return render(request, self.template_name, {
            "form": self.form,
        })

    def post(self, request):
        form = BeanCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/bean/')

