from django.contrib import admin
from .models import Hotel


class HotelAdmin(admin.ModelAdmin):
    # Các trường hiển thị trong danh sách
    list_display = ('hotel_name', 'image', 'address', 'city', 'rating')

    # Các trường cho phép tìm kiếm
    search_fields = ('hotel_name', 'address', 'city')

    # Các trường cho phép lọc
    list_filter = ('city', 'rating')

    # Các trường có thể chỉnh sửa trực tiếp từ danh sách (chỉ dành cho các trường đơn giản)
    list_editable = ('rating',)

    # Các trường hiển thị trong form chỉnh sửa
    fields = ('hotel_name', 'address', 'image', 'city', 'description', 'rating', 'contact_info')

admin.site.register(Hotel, HotelAdmin)
