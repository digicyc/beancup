from django.db import models
from django.contrib.auth.models import User


class BeanBrand(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


class Bean(models.Model):
    DARKNESS = (
        ('L', 'Light'),
        ('M', 'Medium'),
        ('D', 'Dark'),
    )

    name = models.CharField(max_length=200)
    brand = models.ForeignKey(BeanBrand)
    description = models.TextField()
    dark_level = models.CharField(max_length=50, choices=DARKNESS)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    date_added = models.DateTimeField(auto_now=True)


    def __unicode__(self):
        return self.name

