from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['user_name','phone_number','user_mail','purchase_date','purchase_time']
        