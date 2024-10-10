from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

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
    path('', lambda request: HttpResponseRedirect('/admin/')),
    path('', include('e_be_booking_hotel.urls')),  # Đưa các URL của ứng dụng vào dự án
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
