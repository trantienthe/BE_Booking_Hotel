from django.db import models

class Hotel(models.Model):
    hotel_id = models.AutoField(primary_key=True)
    hotel_name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='hotel_images/', blank=True, null=True)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    description = models.TextField()
    rating = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
    contact_info = models.TextField()

    def __str__(self):
        return self.hotel_name