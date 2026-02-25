from django import forms
from .models import TableBooking

class BookingForm(forms.ModelForm):
    class Meta:
        model = TableBooking
        fields = ['name', 'email', 'phone', 'booking_date', 'booking_time', 'number_of_people', 'message']