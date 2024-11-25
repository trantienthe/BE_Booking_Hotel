# Generated by Django 5.1.1 on 2024-11-17 11:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_be_booking_hotel', '0017_voucher_usage_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='voucher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='e_be_booking_hotel.voucher'),
        ),
    ]