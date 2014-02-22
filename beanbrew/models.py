from django.db import models
from django.contrib.auth.models import User
from bean.models import Bean


class Brew(models.Model):
    creator = models.ForeignKey(User)
    bean = models.ForeignKey(Bean)
    ground_level = models.IntegerField(default=1)
    scoops = models.IntegerField(default=1)
    cups_of_water = models.IntegerField(default=1)
    description = models.TextField()
    date_added = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.bean.name

