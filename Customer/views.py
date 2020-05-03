from django.shortcuts import render

def home(request):
    return render(request, 'customer.html')

# Create your views here.
