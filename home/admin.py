from django.contrib import admin
from .models import Event,Booking
# Register your models here.
class CustomeEvent(admin.ModelAdmin):
    prepopulated_fields = {'slug': ("name",)}
    readonly_fields = ['timestamp']
    search_fields = ['name','last_date','timestamp']
    class Meta:
        model=Event
class CustomeBooking(admin.ModelAdmin):
    search_fields = ['visitor_name','phone_number','booking_date']
    list_filter = ['booking_date']
    list_display = ['visitor_name','platinum_seats','gold_seats','silver_seats']



admin.site.register(Event,CustomeEvent)
admin.site.register(Booking,CustomeBooking)