# Generated by Django 5.1.1 on 2024-09-06 17:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_be_booking_hotel', '0002_hotel_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('room_id', models.AutoField(primary_key=True, serialize=False)),
                ('room_type', models.CharField(max_length=100)),
                ('price_per_night', models.DecimalField(decimal_places=2, max_digits=10)),
                ('max_occupancy', models.IntegerField()),
                ('description', models.TextField()),
                ('status', models.CharField(choices=[('available', 'Trống'), ('booked', 'Đã đặt')], max_length=50)),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rooms', to='e_be_booking_hotel.hotel')),
            ],
        ),
    ]