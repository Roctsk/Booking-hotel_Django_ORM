from django.shortcuts import render

from hotel_booking.models import Booking

def booking_list(request):
    booking = Booking.objects.all()
    return render(request,"booking_list.html",{"bookings":booking})

def main_system(request):
    return render(request,"main_system.html")