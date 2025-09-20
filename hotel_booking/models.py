from django.db import models
from django.contrib.auth.models import User

class Hotel(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    city = models.CharField(max_length=100)
    description = models.TextField()
    rating = models.FloatField(default = 0)

    def __str__(self):
        return f"Готель {self.name} в {self.city}"
    

class Room(models.Model):
    hotel = models.ForeignKey(Hotel,on_delete=models.CASCADE, related_name="room")
    room_number = models.CharField(max_length=20)
    room_type = models.CharField(max_length=100)
    beds = models.PositiveIntegerField()
    price_per_hight = models.DecimalField(max_digits=8,decimal_places=2)
    avaible = models.BooleanField(default=True)

    def __str__(self):
        return f"Готель - {self.hotel.name} номер {self.room_number}  "
    

class Booking(models.Model):
    STATUS = [
        ("booked" ,"Заброньвано"),
        ("free" ,"Не заброньовано")
    ]
    user = models.ForeignKey(User,on_delete= models.CASCADE)
    room = models.ForeignKey(Room,on_delete= models.CASCADE)
    start_booking = models.DateTimeField()
    end_booking = models.DateTimeField()
    guests = models.PositiveIntegerField()
    status = models.CharField(max_length=10,choices=STATUS, default="free")


    def __str__(self):
        return f"Бронювання #{self.id} ({self.get_status_display()})"