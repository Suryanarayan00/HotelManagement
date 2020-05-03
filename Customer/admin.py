from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(RoomService)
admin.site.register(LuggageService)
admin.site.register(CustomerContact)
admin.site.register(CheckoutDetail)