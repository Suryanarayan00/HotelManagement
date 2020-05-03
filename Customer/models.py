from django.db import models
from django.conf import settings

# Create your models here.
class CustomerContact(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    room = models.IntegerField()
    datein = models.DateField()
    dateout = models.DateField()
    phone = models.CharField(max_length=100)
    datetimenow = models.DateTimeField(auto_now=True)

class LuggageService(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    datetimenow = models.DateTimeField(auto_now_add=True)

class RoomService(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    service = models.TextField(max_length=100,default=None)
    datetimenow = models.DateTimeField(auto_now_add=True)

class CheckoutDetail(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    datetimenow = models.DateTimeField(auto_now_add=True)