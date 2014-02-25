from django import forms
from bean.models import Bean, BeanBrand
from beanbrew.models import Brew

class BrewCreationForm(forms.Form):
    creator = forms.CharField()
    bean = forms.CharField()
    ground_option = forms.ChoiceField(widget=forms.RadioSelect(), choices=Brew.GRIND_LEVEL)
    ground_level = forms.IntegerField()
    scoops = forms.IntegerField()
    water_bottles = forms.IntegerField()
    description = forms.Textarea()

    def save(self, commit=True):
        bean_clean = self.cleaned_data['bean']
        c_creator = self.cleaned_data['creator']
        c_ground_level = self.cleaned_data['ground_level']
        c_ground_option = self.cleaned_data['ground_option']
        c_scoops = self.cleaned_data['scoops']
        c_water_bottles = self.cleaned_data['water_bottles']
        c_desc = self.cleaned_data['description']

        brew = Brew(
            creator=c_creator, bean=bean_clean, ground_level=c_ground_level,
            ground_option=c_ground_option, scoops=c_scoops, water_bottles=c_water_bottles,
            description=c_desc
        )
        if commit:
            brew.save()
        return brew

