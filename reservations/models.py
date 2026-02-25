from django.db import models

# Create your models here.

class RestaurantSettings(models.Model):
    max_capacity_per_slot = models.IntegerField(default=30)

    def __str__(self):
        return f"Capacity: {self.max_capacity_per_slot}"


class TableBooking(models.Model):
    STATUS_CHOICES = [
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    booking_date = models.DateField()
    booking_time = models.TimeField()
    number_of_people = models.IntegerField()

    message = models.TextField(blank=True, null=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='confirmed'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.booking_date} {self.booking_time}"
