from django.db import models

from e_be_booking_hotel.models import Hotel, User

class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    hotel_id = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    comment = models.TextField()
    review_date = models.DateField()
    img = models.ImageField(upload_to='uploads/%Y/%m/%d/', blank=True, null=True)

    def __str__(self):
        return f"Review {self.review_id} for Hotel {self.hotel_id}"
