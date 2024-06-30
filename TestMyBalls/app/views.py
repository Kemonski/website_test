from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import UsagiInfoForm
from django.contrib import messages
from django.urls import reverse
import random

def home_page(request):
    return render(request, 'Pages/home.html')

def thankyou(request):
    return render(request, 'Pages/purchase.html')

def payment_page(request):
    random_price = random.randint(100, 1000)  # Generate a random price between 100 and 1000
    return render(request, 'Pages/payment.html', {'random_price': random_price})

def bunny_page(request):
    profiles = Profile.objects.all()
    return render(request, 'Pages/bunny.html', {'profiles': profiles})

def profile_detail(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    return render(request, 'Pages/profile_detail.html', {'profile': profile})

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if username == 'admin' and password == '123':
            return redirect(reverse('BUNNYPAGE'))
        else:
            messages.error(request, 'Invalid login credentials')
            return redirect('login')  # Redirect back to the login page
    return render(request, 'Pages/login.html')

def crud_html(request):
    username = Profile.objects.all()
    details = UsagiInfo.objects.all()
    context = {
        'username': username,
        'details': details,
    }
    return render(request, 'Pages/bunny_crud.html', context)

def usagiinfo_create(request):
    if request.method == "POST":
        form = UsagiInfoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('BUNNYPAGE')
    else:
        form = UsagiInfoForm()
    return render(request, 'Pages/usagiinfo_form.html', {'form': form})

def usagiinfo_update(request, pk):
    usagiinfo = get_object_or_404(UsagiInfo, pk=pk)
    if request.method == "POST":
        form = UsagiInfoForm(request.POST, instance=usagiinfo)
        if form.is_valid():
            form.save()
            return redirect('BUNNYPAGE')
    else:
        form = UsagiInfoForm(instance=usagiinfo)
    return render(request, 'Pages/usagiinfo_form.html', {'form': form})

def usagiinfo_delete(request, pk):
    usagiinfo = get_object_or_404(UsagiInfo, pk=pk)
    if request.method == "POST":
        usagiinfo.delete()
        return redirect('BUNNYPAGE')
    return render(request, 'Pages/usagiinfo_confirm_delete.html', {'usagiinfo': usagiinfo})
