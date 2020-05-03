from django.db import models
from django.conf import settings
# Create your models here.


class TodaySpecialBreakfast(models.Model):
    Breakfast = models.CharField(max_length=100, default=None)

class TodaySpecialLunch(models.Model):
    Lunch = models.CharField(max_length=100, default=None)

class TodaySpecialDinner(models.Model):
    Dinner = models.CharField(max_length=100, default=None)

class MenuBreakfast(models.Model):
    Breakfast = models.CharField(max_length=100, default=None)
    Price = models.IntegerField()

class MenuLunch(models.Model):
    Lunch = models.CharField(max_length=100, default=None)
    Price = models.IntegerField()

class MenuDinner(models.Model):
    Dinner = models.CharField(max_length=100, default=None)
    Price = models.IntegerField()

class NonvegBreakfast(models.Model):
    Breakfast = models.CharField(max_length=100, default=None)
    Price = models.IntegerField()

class NonvegLunch(models.Model):
    Lunch = models.CharField(max_length=100, default=None)
    Price = models.IntegerField()

class NonvegDinner(models.Model):
    Dinner = models.CharField(max_length=100, default=None)
    Price = models.IntegerField()