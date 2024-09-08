from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from e_be_booking_hotel.views import HotelViewSet, UserViewSet

# Tạo router và đăng ký viewsets
router = DefaultRouter()
router.register(r'hotels', HotelViewSet)
router.register(r'user', UserViewSet)

# Tạo schema view cho Swagger
schema_view = get_schema_view(
   openapi.Info(
      title="Hotel API",
      default_version='v1',
      description="API documentation for the Hotel model",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@hotel.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),  # Đưa các URL của ứng dụng vào dự án
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
