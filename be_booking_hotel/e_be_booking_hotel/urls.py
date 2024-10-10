from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HotelViewSet, RoomViewSet, UserViewSet, UtilitiesViewSet, AreaViewSet, LoginViewSet, SliderViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register(r'hotels', HotelViewSet)  # Đăng ký ViewSet với router
router.register(r'room', RoomViewSet)
router.register(r'user', UserViewSet)
router.register(r'utilities', UtilitiesViewSet)
router.register(r'area', AreaViewSet)
router.register(r'login', LoginViewSet, basename='login')
router.register(r'slider', SliderViewSet)

urlpatterns = [
    path('', include(router.urls)),  # Bao gồm các URL từ router
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # path('login/', LoginViewSet.as_view(), name='login'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
