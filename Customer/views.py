from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from Manager.models import TodaySpecialDinner, TodaySpecialLunch, TodaySpecialBreakfast, NonvegBreakfast, NonvegLunch, NonvegDinner,MenuBreakfast, MenuDinner, MenuLunch
from .models import CustomerContact, LuggageService, RoomService, CheckoutDetail

def home(request):
    todayspecialbreakfast = TodaySpecialBreakfast.objects.all()
    todayspecialdinner =TodaySpecialDinner.objects.all()
    todayspeciallunch =TodaySpecialLunch.objects.all()
    nonvegbreakfast = NonvegBreakfast.objects.all()
    nonveglunch = NonvegLunch.objects.all()
    nonvegdinner = NonvegDinner.objects.all()
    menbreakfast = MenuBreakfast.objects.all()
    menudinner = MenuDinner.objects.all()
    menulunch = MenuLunch.objects.all()
    return render(request, 'customer.html', {'todayspecialbreakfast':todayspecialbreakfast , 'todayspecialdinner': todayspecialdinner, 'todayspeciallunch': todayspeciallunch, 'nonvegbreakfast':nonvegbreakfast , 'nonveglunch':nonveglunch , 'nonvegdinner':nonvegdinner , 'menbreakfast':menbreakfast , 'menudinner':menudinner , 'menulunch': menulunch, })

def logout(request):
        user = request.user
        checkoutdetail = CheckoutDetail(user=user)
        checkoutdetail.save()
        auth.logout(request)
        return redirect('/')
# Create your views here.

def contact(request):
    # DateField
    if request.method=='POST':
        room = request.POST['room']
        datein = request.POST['datein']
        dateout = request.POST['dateout']
        phone = request.POST['phone']
        user = request.user
        customer = CustomerContact(user=user, room=room, datein=datein, dateout=dateout, phone=phone)
        customer.save()
        return redirect('Customer/home')

def roomservice(request):
    if request.method == 'POST':
        user  = request.user
        service = request.POST['service']
        servicerequest = RoomService(user=user, service=service)
        servicerequest.save()
        return redirect('Customer/home')
    else:
        return redirect('home')

def luggageservice(request):
    if request.method == 'POST':
        user = request.user
        luggage = luggageservice(user=user)
        luggage.save()
        return redirect('Customer/home')
    else:
        return redirect('home')