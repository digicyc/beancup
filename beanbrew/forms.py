from django import forms
from bean.models import Bean, BeanBrand

class BrewCreationForm(forms.Form):
    creator = forms.CharField()
    bean = forms.CharField()
    group_level = forms.IntegerField()
    scoops = forms.IntegerField()
    cups_of_water = forms.IntegerField()
    description = forms.Textarea()

    def save(self, commit=True):
        # Check if bean exists?
        bean_clean = self.cleaned_data['bean']
        bean_obj = Bean.objects.get(name=bean_clean)
