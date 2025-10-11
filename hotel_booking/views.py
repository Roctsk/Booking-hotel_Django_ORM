from django.shortcuts import render , redirect

from hotel_booking.models import Booking
from hotel_booking.forms import BookingForm
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'system/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'system/login.html', {'form': form})





def booking_list_as_admin(request):
    booking = Booking.objects.all()
    return render(request,"booking_list_as_admin.html",{"bookings":booking})

def main_system(request):
    return render(request,"main_system.html")

def booking_as_admin(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            return redirect("booking_list_as_admin")
    else:
        form = BookingForm()
    return render(request,"booking_as_admin.html",{"form":form})

def my_booking_as_admin(request):
    if request.user.is_authenticated:
        bookings = Booking.objects.filter(user = request.user)
    else:
        bookings = []
    return render(request,"my_booking_as_admin.html",{"bookings": bookings})
    



@login_required
def booking_as_user(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()  
            messages.success(request, '✅ Ви успішно забронювали номер!')
            return redirect("/")    
    else:
        form = BookingForm()
    return render(request,"booking_as_user.html",{"form":form})


