from django.contrib import admin
from beanbrew.models import Brew


class BrewAdmin(admin.ModelAdmin):
    list_display = ('creator', 'bean', 'scoops', 'cups_of_water')


admin.site.register(Brew, BrewAdmin)