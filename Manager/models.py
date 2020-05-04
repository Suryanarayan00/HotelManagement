from django.db import models
from django.conf import settings
# Create your models here.


class TodaySpecial(models.Model):
    Breakfast = models.CharField(max_length=100, default=None)
    Lunch = models.CharField(max_length=100, default=None)
    Dinner = models.CharField(max_length=100, default=None)

class Menu(models.Model):
    Breakfast = models.CharField(max_length=100, default=None)
    PriceBreakfast = models.IntegerField()
    Lunch = models.CharField(max_length=100, default=None)
    PriceLunch = models.IntegerField()
    Dinner = models.CharField(max_length=100, default=None)
    PriceDinner = models.IntegerField()


class Nonveg(models.Model):
    Breakfast = models.CharField(max_length=100, default=None)
    Price = models.IntegerField()
    Lunch = models.CharField(max_length=100, default=None)
    Price = models.IntegerField()
    Dinner = models.CharField(max_length=100, default=None)
    Price = models.IntegerField()
