from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from Manager.models import TodaySpecial, Menu, Nonveg
from .models import CustomerContact, LuggageService, RoomService, CheckoutDetail, FoodService

def home(request):
    todayspecial = TodaySpecial.objects.all()
    menu = Menu.objects.all()
    nonveg = Nonveg.objects.all()
    return render(request, 'customer.html', {'todayspecial':todayspecial , 'menu': menu, 'nonveg': nonveg })

def food(request):
    if request.method == 'POST':
        Breakfast = request.POST['Breakfast']
        Lunch = request.POST['Lunch']
        Dinner = request.POST['Dinner']
        user = request.user
        foodservice = FoodService(user=user, Breakfast=Breakfast, Lunch=Lunch, Dinner=Dinner)
        foodservice.save()
        # if request.path.startswith('Customer/Customer'):
        return redirect('changeurl')

def logout(request):
    user = request.user
    checkoutdetail = CheckoutDetail(user=user)
    checkoutdetail.save()
    user = User.objects.filter(id=request.user.pk).delete()
    User.objects.filter(pk=request.user.pk).update(is_active=False, email=None)
    # auth.logout(request)
    return redirect('/')
# Create your views here.

def Logout(request):
    auth.logout(request)
    return redirect('/')

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
        # if request.path.startswith('Customer/Customer'):
        return redirect('changeurl')
        # else:
        # return redirect('Customer/home')

def roomservice(request):
    if request.method == 'POST':
        user  = request.user
        service = request.POST['service']
        servicerequest = RoomService(user=user, service=service)
        servicerequest.save()
        # if request.path.startswith('Customer/'):
        return redirect('changeurl')
        # return redirect('Customer/home')
    # else:
    #     return redirect('home')

def luggageservice(request):
    if request.method == 'POST':
        user = request.user
        luggage = LuggageService(user=user)
        luggage.save()
    #     if request.path.startswith('Customer/'):
        return redirect('changeurl')
    #     return redirect('Customer/home')
    # else:
    #     return redirect('home')