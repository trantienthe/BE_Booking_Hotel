from datetime import timedelta

from django.db import models
from django.utils import timezone

from e_be_booking_hotel.models import User
from .voucher import Voucher


class Order(models.Model):
    PAYMENT_METHODS = [
        ('atm', 'ATM'),
        ('Tiền mặt', 'Tiền mặt'),
        ('postpaid', 'Trả sau'),
        ('vnpay', 'VNPAY'),
        ('zalopay', 'ZALOPAY'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    payment_method = models.CharField(max_length=10, choices=PAYMENT_METHODS)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='pending')
    voucher = models.ForeignKey(Voucher, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"Đơn hàng {self.id} của {self.full_name} - Trạng thái: {self.status}"




