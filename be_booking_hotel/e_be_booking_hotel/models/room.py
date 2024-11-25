from django.db import models
from .area import Area

class Room(models.Model):
    ROOM_STATUS_CHOICES = [
        ('available', 'Trống'),
        ('booked', 'Đã đặt'),
    ]

    room_id = models.AutoField(primary_key=True)  # Tạo RoomID tự động tăng
    area = models.ForeignKey(Area, on_delete=models.CASCADE, related_name='rooms')  # ForeignKey liên kết với bảng Hotels
    room_type = models.CharField(max_length=100)  # Loại phòng
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)  # Giá mỗi đêm
    max_occupancy = models.IntegerField()  # Số lượng người tối đa
    description = models.TextField()  # Mô tả phòng
    thumbnail = models.ImageField(upload_to='uploads/%Y/%m/%d/')
    status = models.CharField(max_length=50, choices=ROOM_STATUS_CHOICES, default='available', blank=True)  # Trạng thái phòng mặc định là 'available'

    def get_images(self):
        return self.images.all()

    def __str__(self):
        return f"Room {self.room_id} - {self.room_type} at {self.area.name}"
