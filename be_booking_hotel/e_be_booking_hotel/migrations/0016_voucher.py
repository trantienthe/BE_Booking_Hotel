# Generated by Django 5.1.1 on 2024-11-17 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_be_booking_hotel', '0015_alter_review_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Voucher',
            fields=[
                ('voucher_id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID Khuyến Mãi')),
                ('code', models.CharField(max_length=50, unique=True, verbose_name='Mã Khuyến Mãi')),
                ('discount_percentage', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Phần Trăm Giảm Giá')),
                ('start_date', models.DateTimeField(verbose_name='Ngày Bắt Đầu')),
                ('end_date', models.DateTimeField(verbose_name='Ngày Kết Thúc')),
                ('is_active', models.BooleanField(default=True, verbose_name='Kích Hoạt')),
            ],
        ),
    ]