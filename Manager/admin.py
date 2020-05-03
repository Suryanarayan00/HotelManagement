from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(TodaySpecialBreakfast)
admin.site.register(TodaySpecialLunch)
admin.site.register(TodaySpecialDinner)

admin.site.register(MenuBreakfast)
admin.site.register(MenuLunch)
admin.site.register(MenuDinner)

admin.site.register(NonvegBreakfast)
admin.site.register(NonvegDinner)
admin.site.register(NonvegLunch)


