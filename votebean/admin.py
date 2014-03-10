from django.contrib import admin
from .models import VoteBean


class VoteBeanAdmin(admin.ModelAdmin):
    list_display = ('voter', 'bean_type', 'vote_count')

admin.site.register(VoteBean, VoteBeanAdmin)
