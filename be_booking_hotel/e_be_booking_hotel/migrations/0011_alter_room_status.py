# Generated by Django 5.1.1 on 2024-11-07 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_be_booking_hotel', '0010_remove_order_room_orderdetail_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='status',
            field=models.CharField(blank=True, choices=[('available', 'Trống'), ('booked', 'Đã đặt')], default='available', max_length=50),
        ),
    ]
