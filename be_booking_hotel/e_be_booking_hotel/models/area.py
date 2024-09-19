from django.db import models

from .hotel import Hotel


class Area(models.Model):
    area_id = models.AutoField(primary_key=True)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE,
                              related_name='rooms')  # ForeignKey liên kết với bảng Hotels
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name} - {self.hotel.hotel_name}'
