from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HotelViewSet

router = DefaultRouter()
router.register(r'hotels', HotelViewSet)  # Đăng ký ViewSet với router

urlpatterns = [
    path('', include(router.urls)),  # Bao gồm các URL từ router
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
