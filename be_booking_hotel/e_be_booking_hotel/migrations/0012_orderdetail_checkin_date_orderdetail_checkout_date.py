# Generated by Django 5.1.1 on 2024-11-12 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_be_booking_hotel', '0011_alter_room_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderdetail',
            name='checkin_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='orderdetail',
            name='checkout_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
