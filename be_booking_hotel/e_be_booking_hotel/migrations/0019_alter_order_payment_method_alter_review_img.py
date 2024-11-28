# Generated by Django 5.1.1 on 2024-11-28 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_be_booking_hotel', '0018_order_voucher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment_method',
            field=models.CharField(choices=[('atm', 'ATM'), ('Tiền mặt', 'Tiền mặt'), ('postpaid', 'Trả sau'), ('vnpay', 'VNPAY'), ('zalopay', 'ZALOPAY')], max_length=10),
        ),
        migrations.AlterField(
            model_name='review',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/%Y/%m/%d/'),
        ),
    ]