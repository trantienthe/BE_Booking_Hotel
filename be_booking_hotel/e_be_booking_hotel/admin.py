from django.contrib import admin
from django.utils.html import format_html

from .models import Hotel, Utilities, RoomUtilities, Area, RoomImages
from .models import User
from .models import Room

class AreaAdmin(admin.ModelAdmin):
    list_display = ('name', 'hotel')
    search_fields = ('name',)
    fields  = ('name', 'hotel')

class RoomUtilitiesAdmin(admin.ModelAdmin):
    list_display = ('id_room_utilities','room_id', 'utilities_id')

class UtilitiesAdmin(admin.ModelAdmin):
    list_display = ('utilities_id', 'name')
    search_fields = ('name',)
    fields = ('name',)

class RoomUtilitiesInline(admin.TabularInline):
    model = RoomUtilities
    extra = 1
    fields = ('utilities',)

class RoomImagesInline(admin.TabularInline):
    model = RoomImages
    extra = 1

class RoomAdmin(admin.ModelAdmin):
    list_display = ('room_id', 'area', 'room_type', 'price_per_night', 'max_occupancy','thumbnail_display', 'description', 'status', 'utilities_display')
    list_filter = ('area', 'room_type', 'status')
    search_fields = ('room_type', 'description', 'status')
    fields = ('area', 'room_type', 'price_per_night', 'max_occupancy','thumbnail', 'description', 'status')
    inlines = [RoomImagesInline, RoomUtilitiesInline]

    def utilities_display(self, obj):
        utilities = obj.room_utilities.filter(room=obj)
        return ', '.join([utility.utilities.name for utility in utilities])

    utilities_display.short_description = 'Utilities'

    def thumbnail_display(self, obj):
        if obj.thumbnail:
            return format_html('<img src="{}" width="100" height="100" />', obj.thumbnail.url)
        return "No Thumbnail"
    thumbnail_display.short_description = 'Thumbnail'

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_superuser', 'is_active')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    search_fields = ('username', 'email')
    fields  = ('username', 'email', 'password', 'first_name','last_name', 'avatar')

class HotelAdmin(admin.ModelAdmin):
    # Các trường hiển thị trong danh sách
    list_display = ('hotel_name', 'image_display', 'address', 'city', 'rating')

    # Các trường cho phép tìm kiếm
    search_fields = ('hotel_name', 'address', 'city')

    # Các trường cho phép lọc
    list_filter = ('city', 'rating')

    # Các trường có thể chỉnh sửa trực tiếp từ danh sách (chỉ dành cho các trường đơn giản)
    list_editable = ('rating',)

    # Các trường hiển thị trong form chỉnh sửa
    fields = ('hotel_name', 'address', 'image', 'city', 'description', 'contact_info')

    def image_display(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" height="100" />', obj.image.url)
        return "No Thumbnail"
    image_display.short_description = 'Image'

admin.site.register(Room, RoomAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Hotel, HotelAdmin)
admin.site.register(Utilities, UtilitiesAdmin)
# admin.site.register(RoomUtilities, RoomUtilitiesAdmin)
admin.site.register(Area, AreaAdmin)

