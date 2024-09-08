from django.contrib import admin

from .models import Hotel
from .models import User
from .models import Room

class RoomAdmin(admin.ModelAdmin):
    list_display = ('room_id', 'hotel', 'room_type', 'price_per_night', 'max_occupancy', 'description', 'status')
    list_filter = ('hotel', 'room_type', 'status')
    search_fields = ('room_type', 'description', 'status')
    fields = ('hotel', 'room_type', 'price_per_night', 'max_occupancy', 'description', 'status')

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_superuser', 'is_active')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    search_fields = ('username', 'email')
    fields  = ('username', 'email', 'password', 'first_name','last_name', 'avatar')

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

admin.site.register(Room, RoomAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Hotel, HotelAdmin)