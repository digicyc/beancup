from django.db import models
from django.contrib.auth.models import User
from bean.models import Bean

class VoteBean(models.Model):
    voter = models.ForeignKey(User)
    bean_type = models.ForeignKey(Bean, unique=True)
    vote_count = models.IntegerField()
    date_added = models.DateTimeField(auto_now=True)
