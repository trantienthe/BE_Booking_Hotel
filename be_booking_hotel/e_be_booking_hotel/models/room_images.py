from django.db import models

from e_be_booking_hotel.models import Room

class RoomImages(models.Model):
    image_id = models.AutoField(primary_key=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='images')
    url = models.ImageField(upload_to='uploads/%Y/%m/%d/')

    def __str__(self):
        return f"ImageID: {self.image_id} for RoomID: {self.room.room_id}"