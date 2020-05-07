from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from Customer.models import CheckoutDetail, RoomService, LuggageService, CustomerContact, FoodService
# Create your views here.
def home(request):
    checkoutdetail = CheckoutDetail.objects.all()
    roomservice = RoomService.objects.all()
    luggageservice = LuggageService.objects.all()
    customercontact = CustomerContact.objects.all()
    foodservice = FoodService.objects.all()

    return render(request, 'reception.html', {'checkoutdetail': checkoutdetail, 'roomservice':roomservice, 'luggageservice':luggageservice, 'foodservice':foodservice, 'customercontact':customercontact})

def logout(request):
    auth.logout(request)
    return redirect('/')

