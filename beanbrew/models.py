from django.db import models
from django.contrib.auth.models import User
from bean.models import Bean


class Brew(models.Model):
    GRIND_LEVEL = (
        ('EF', 'Extra Fine'),
        ('F', 'Fine'),
        ('M', 'Medium'),
        ('C', 'Course'),
    )

    creator = models.ForeignKey(User)
    bean = models.ForeignKey(Bean)
    ground_option = models.CharField(max_length=50, choices=GRIND_LEVEL)
    ground_level = models.IntegerField(default=1, max_length=1)
    scoops = models.IntegerField(default=1)
    water_bottles = models.CharField(max_length=2, default="1")
    description = models.TextField()
    date_added = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.bean.name

