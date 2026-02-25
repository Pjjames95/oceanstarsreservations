from django.shortcuts import render

# Create your views here.
from django.db.models import Sum
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import TableBooking, RestaurantSettings
from django.db import transaction



@api_view(['POST'])
@transaction.atomic #make it more safe by wrapping it around a transaction
def create_booking(request):
    
    name = request.data.get('name')
    email = request.data.get('email')
    phone = request.data.get('phone')
    booking_date = request.data.get('date')
    booking_time = request.data.get('time')
    number_of_people = int(request.data.get('people', 0))
    message = request.data.get('message', '')

    if not all([name, email, phone, booking_date, booking_time, number_of_people]):
        return Response({"error": "Missing required fields"}, status=400)

    # 1️⃣ Get restaurant capacity
    settings = RestaurantSettings.objects.first()
    capacity = settings.max_capacity_per_slot if settings else 30

    # 2️⃣ Calculate already booked people
    total_booked = TableBooking.objects.filter(
        booking_date=booking_date,
        booking_time=booking_time,
        status='confirmed'
    ).aggregate(total=Sum('number_of_people'))['total'] or 0

    # 3️⃣ Check availability
    if total_booked + number_of_people > capacity:
        return Response(
            {"error": "No availability for selected time slot"},
            status=400
        )

    # 4️⃣ Create booking
    TableBooking.objects.create(
        name=name,
        email=email,
        phone=phone,
        booking_date=booking_date,
        booking_time=booking_time,
        number_of_people=number_of_people,
        message=message
    )

    return Response({"message": "Booking confirmed"}, status=201)