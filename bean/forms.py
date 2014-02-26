from django import forms
from bean.models import Bean, BeanBrand

class BeanCreationForm(forms.Form):
    creator = forms.CharField()
    brand = forms.CharField()
    description = forms.Textarea()
    dark_level = forms.CharField()
    price = forms.DecimalField(max_digits=8, decimal_places=2)

    def save(self, commit=True):
        c_name = self.cleaned_data['name']
        c_brand = self.cleaned_data['brand']
        c_description = self.cleaned_data['description']
        c_dark_level = self.cleaned_data['dark_level']
        c_price = self.cleaned_data['price']

        bean = Bean(
            name=c_name, brand=c_brand, description=c_description,
            dark_level=c_dark_level, price=c_price
        )

        if commit:
            bean.save()
        return bean