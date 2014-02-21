from django.db import models
from django.contrib.auth.models import User
from bean.models import Bean

class VoteBean(models.Model):
    owner = models.ForeignKey(User)
    vote_count = models.IntegerField()
    bean_type = models.ForeignKey(Bean)
    date_added = models.DateTimeField(auto_now=True)
