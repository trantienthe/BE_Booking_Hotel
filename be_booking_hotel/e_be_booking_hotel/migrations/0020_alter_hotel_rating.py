# Generated by Django 5.1.1 on 2024-11-29 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_be_booking_hotel', '0019_alter_order_payment_method_alter_review_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='rating',
            field=models.FloatField(blank=True, null=True),
        ),
    ]