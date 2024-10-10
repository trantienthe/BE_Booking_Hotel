# Generated by Django 5.1.1 on 2024-10-10 15:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_be_booking_hotel', '0003_alter_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('slider_id', models.AutoField(primary_key=True, serialize=False)),
                ('image_url', models.ImageField(upload_to='uploads/%Y/%m/%d/')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('order', models.IntegerField(default=0)),
                ('room', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='e_be_booking_hotel.room')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
    ]