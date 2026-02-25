from django.contrib import admin

# Register your models here.
from .models import TableBooking

@admin.register(TableBooking)
class TableBookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'booking_date', 'booking_time', 'number_of_people', 'status')
    list_filter = ('booking_date', 'status')
    search_fields = ('name', 'phone')
