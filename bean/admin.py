from django.contrib import admin
from bean.models import Bean, BeanBrew, BeanBrand


class BeanBrewAdmin(admin.ModelAdmin):
    list_display = ('creator', 'bean', 'scoops', 'cups_of_water')


class BeanAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'dark_level', 'price')

class BeanBrandAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Bean, BeanAdmin)
admin.site.register(BeanBrew, BeanBrewAdmin)
admin.site.register(BeanBrand, BeanBrandAdmin)
