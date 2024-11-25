from django.contrib import admin
from django.utils.html import format_html

from .models import Hotel, Utilities, RoomUtilities, Area, RoomImages, Cart, Order, OrderDetail, Review, Voucher
from .models import User
from .models import Room
from .models import Slider

class VoucherAdmin(admin.ModelAdmin):
    list_display = ('voucher_id', 'code', 'discount_percentage', 'start_date', 'end_date', 'is_active', 'usage_count')
    list_filter = ('is_active', 'start_date', 'end_date')
    search_fields = ('code',)
    ordering = ('-start_date',)

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('review_id', 'hotel_id', 'user_id', 'rating', 'comment', 'review_date', 'img_display')
    list_filter = ('hotel_id', 'user_id')
    search_fields = ('hotel_id','user_id')
    fields = ( 'hotel_id', 'user_id', 'rating', 'comment', 'review_date')

    def img_display(self, obj):
        if obj.img:
            return format_html('<img src="{}" width="50" height="50" />', obj.img)
        return "No Image"
    img_display.short_description = 'Image'

class OrderDetailAdmin(admin.ModelAdmin):
    list_display = ('order', 'room', 'price', 'checkin_date', 'checkout_date')
    list_filter = ('order', 'room')
    search_fields = ('order__id', 'room__room_type')
    fields = ('order', 'room', 'price', 'checkin_date', 'checkout_date')
    readonly_fields = ('order', 'room', 'price', 'checkin_date', 'checkout_date')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'email', 'phone_number', 'voucher', 'payment_method', 'total_price', 'order_date', 'status', 'user_id')  # Các trường hiển thị trong danh sách
    list_filter = ('status', 'user')  # Bộ lọc để cho phép phân loại theo trạng thái, người dùng và phòng
    search_fields = ('user__username', 'status')  # Bật tính năng tìm kiếm theo tên người dùng và loại phòng
    readonly_fields = ('order_date', 'total_price')  # Các trường không nên được chỉnh sửa

    def has_add_permission(self, request):
        return True  # Cho phép thêm đơn hàng từ admin

    def has_delete_permission(self, request, obj=None):
        return True  # Cho phép xóa đơn hàng từ admin

    def has_change_permission(self, request, obj=None):
        return True  # Cho phép thay đổi đơn hàng từ admin



class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'room', 'checkin_date', 'checkout_date', 'total_days', 'total_price')  # Các trường hiển thị trong danh sách
    list_filter = ('user', 'room')  # Bộ lọc theo người dùng và phòng
    readonly_fields = ('user','total_price', 'checkin_date', 'checkout_date', 'room', 'total_days')

    def has_add_permission(self, request):
        return False  # Không cho phép thêm giỏ hàng từ admin

    def total_days(self, obj):
        if obj.checkin_date and obj.checkout_date:
            return (obj.checkout_date - obj.checkin_date).days
        return 0  # Trả về 0 nếu không có thông tin ngày

    total_days.short_description = 'Tổng số ngày'

    def has_delete_permission(self, request, obj=None):
        return True  # Cho phép xóa giỏ hàng từ admin


class SliderAdmin(admin.ModelAdmin):
    list_display = ('slider_id', 'image_url','video_url', 'title', 'order', 'room')
    search_fields = ('title', 'room__room_type')
    fields = ('image_url','video_url',  'title', 'description', 'room', 'order')
    ordering = ('order',)

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
admin.site.register(Slider, SliderAdmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderDetail, OrderDetailAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Voucher, VoucherAdmin)

