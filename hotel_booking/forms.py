from django import forms
from hotel_booking.models import Booking

class BookingForm(forms.ModelForm):
    class Meta():
        model = Booking
        fields = [
            "room","start_booking","end_booking","guests"
        ]

        widgets = {
            "start_booking": forms.DateInput(attrs={
                "type": "date", 
                "class": "form-control"
            }
            ),            
            "end_booking": forms.DateInput(attrs={
                "type": "date", 
                "class": "form-control"
            })}

