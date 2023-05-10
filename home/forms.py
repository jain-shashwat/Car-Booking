from django.forms import ModelForm,DateField,Textarea,TextInput,Select
from .models import  Booking
class BookingForm(ModelForm):

    class Meta:
        model=Booking
        fields=['visitor_name','phone_number','event_name','time_preference','platinum_seats','gold_seats','silver_seats' ,'booking_date']
        widgets={
            'booking_date':TextInput(attrs={'type':'date','class':'form-control','type':'hidden'}),
            'visitor_name':TextInput(attrs={'class':'form-control'}),
            'phone_number':TextInput(attrs={'class':'form-control'}),
            'event_name':TextInput(attrs={'class':'form-control'}),
            'time_preference':Select(attrs={'class':'form-control'}),
            'platinum_seats':TextInput(attrs={'class':'form-control'}),
            'gold_seats':TextInput(attrs={'class':'form-control'}),
            'silver_seats':TextInput(attrs={'class':'form-control'}),
            'event_name':TextInput(attrs={'type':'hidden'})
            }