from django.db import models
from poetry.json import ValidationError

from .room import Room

class Slider(models.Model):
    slider_id = models.AutoField(primary_key=True)  # Tạo slider_id tự động tăng
    image_url = models.ImageField(upload_to='uploads/images/%Y/%m/%d/', blank=True, null=True)  # Hình ảnh slider
    video_url = models.FileField(upload_to='uploads/videos/%Y/%m/%d/', blank=True, null=True)  # Video slider
    title = models.CharField(max_length=255, blank=True, null=True)  # Tiêu đề tùy chọn
    description = models.TextField(blank=True, null=True)  # Mô tả tùy chọn
    room = models.ForeignKey(Room, on_delete=models.CASCADE, blank=True, null=True)  # Khóa ngoại liên kết với Room, cho phép NULL
    order = models.IntegerField(default=0)  # Thứ tự hiển thị của slider

    def __str__(self):
        return self.title if self.title else f"Slider {self.slider_id}"

    class Meta:
        ordering = ['order']  # Sắp xếp theo thứ tự ưu tiên

