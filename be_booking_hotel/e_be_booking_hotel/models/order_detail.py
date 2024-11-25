from django.db import models

from e_be_booking_hotel.models import Room, Order, Cart


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    checkin_date = models.DateField(null=True, blank=True)  # Làm cho trường nullable
    checkout_date = models.DateField(null=True, blank=True)  # Làm cho trường nullable

    def __str__(self):
        return f"Chi tiết đơn hàng của {self.order.user} cho phòng {self.room}"
