from django.db import models
from e_be_booking_hotel.models import Room, User


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='carts')
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    checkin_date = models.DateField()
    checkout_date = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2, editable=False)

    def __str__(self):
        return f"Giỏ của {self.user.last_name} - Phòng {self.room.room_id}"

    def save(self, *args, **kwargs):
        self.total_price = self.room.price_per_night * (self.checkout_date - self.checkin_date).days  # Tính tổng giá
        super().save(*args, **kwargs)  # Gọi phương thức save gốc
