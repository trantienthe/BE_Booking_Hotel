from django.db import models

class Voucher(models.Model):
    voucher_id = models.AutoField(primary_key=True, verbose_name="ID Khuyến Mãi")
    code = models.CharField(max_length=50, unique=True, verbose_name="Mã Khuyến Mãi")
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Phần Trăm Giảm Giá")
    start_date = models.DateTimeField(verbose_name="Ngày Bắt Đầu")
    end_date = models.DateTimeField(verbose_name="Ngày Kết Thúc")
    is_active = models.BooleanField(default=True, verbose_name="Kích Hoạt")
    usage_count = models.PositiveIntegerField(default=0, verbose_name="Số lượt Sử Dụng")

    def __str__(self):
        return self.code
