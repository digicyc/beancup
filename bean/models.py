from django.db import models


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

    @property
    def price(self):
        return "$%s" % self.price


    def __unicode__(self):
        return self.name


class BeanBrew(models.Model):
    scoops = models.IntegerField(default=1)
    cups_of_water = models.IntegerField(default=1)
    description = models.TextField()

