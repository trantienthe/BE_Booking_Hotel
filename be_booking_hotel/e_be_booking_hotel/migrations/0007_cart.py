# Generated by Django 5.1.1 on 2024-10-10 16:45

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_be_booking_hotel', '0006_slider_video_url_alter_slider_image_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checkin_date', models.DateField()),
                ('checkout_date', models.DateField()),
                ('total_price', models.DecimalField(decimal_places=2, editable=False, max_digits=10)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='e_be_booking_hotel.room')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='carts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
