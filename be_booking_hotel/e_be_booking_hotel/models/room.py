from django.db import models

from e_be_booking_hotel.models import Hotel


class Room(models.Model):
    ROOM_STATUS_CHOICES = [
        ('available', 'Trống'),
        ('booked', 'Đã đặt'),
    ]

    room_id = models.AutoField(primary_key=True)  # Tạo RoomID tự động tăng
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='rooms')  # ForeignKey liên kết với bảng Hotels
    room_type = models.CharField(max_length=100)  # Loại phòng
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)  # Giá mỗi đêm
    max_occupancy = models.IntegerField()  # Số lượng người tối đa
    description = models.TextField()  # Mô tả phòng
    status = models.CharField(max_length=50, choices=ROOM_STATUS_CHOICES)  # Trạng thái phòng

    def __str__(self):
        return f"Room {self.room_id} - {self.room_type} at {self.hotel.hotel_name}"