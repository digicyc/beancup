from django import forms
from bean.models import Bean, BeanBrand
from beanbrew.models import Brew

class BrewCreationForm(forms.Form):
    # Bean form
    bean = forms.CharField()
    dark_choices = forms.ChoiceField(widget=forms.RadioSelect(), choices=Bean.DARKNESS)
    bean_brand = forms.ModelChoiceField(widget=forms.Select(), queryset=BeanBrand.objects.all())
    bean_desc = forms.CharField()

    # Brew form
    ground_option = forms.ChoiceField(widget=forms.RadioSelect(), choices=Brew.GRIND_LEVEL)
    ground_level = forms.IntegerField()
    scoops = forms.IntegerField()
    water_bottles = forms.IntegerField()
    description = forms.Textarea()


    def save(self, user, commit=True):
        # Bean Stuff
        bean_name = self.cleaned_data['bean']
        dark_level = self.cleaned_data['dark_level']
        bean_brand = self.cleaned_data['brand']
        bean_desc = self.cleaned_data['bean_desc']


        # Brew Stuff
        ground_level = self.cleaned_data['ground_level']
        ground_option = self.cleaned_data['ground_option']
        scoops = self.cleaned_data['scoops']
        water_bottles = self.cleaned_data['water_bottles']
        desc = self.cleaned_data['description']


        try:
            brand = BeanBrand.objects.get(name=bean_brand)
        except BeanBrand.DoesNotExist:
            brand = BeanBrand(name=bean_brand)
            brand.save()

        try:
            bean = Bean.objects.get(name=bean_name, brand=brand)
        except Bean.DoesNotExist:
            bean = Bean(
                name=bean_name, brand=brand, description=bean_desc, dark_level=dark_level,
            )
            bean.save()

        brew = Brew(
            creator=user, bean=bean, ground_level=ground_level,
            ground_option=ground_option, scoops=scoops, water_bottles=water_bottles,
            description=desc
        )
        if commit:
            brew.save()

        return brew

