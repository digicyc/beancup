from django.contrib import admin
from bean.models import Bean, BeanBrand


class BeanAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'dark_level', 'price')


class BeanBrandAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Bean, BeanAdmin)
admin.site.register(BeanBrand, BeanBrandAdmin)
