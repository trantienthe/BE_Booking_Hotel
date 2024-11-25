# Generated by Django 5.1.1 on 2024-11-06 17:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_be_booking_hotel', '0009_remove_orderdetail_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='room',
        ),
        migrations.AddField(
            model_name='orderdetail',
            name='order',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='e_be_booking_hotel.order'),
            preserve_default=False,
        ),
    ]