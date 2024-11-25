from os.path import basename

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import HotelViewSet, RoomViewSet, UserViewSet, UtilitiesViewSet, AreaViewSet, LoginViewSet, SliderViewSet, \
    CartViewSet, OrderViewSet, OrderDetailViewSet, ReviewViewSet, VoucherViewSet, SearchViewSet
from .zalopay import CreateOrderZaloPayView, CheckoutZaloPayView
from .zalopay.zalopay_callback import ZaloPayCallback
from .zalopay.zalopay_status import ZaloPayOrderStatus

router = DefaultRouter()
router.register(r'hotels', HotelViewSet)  # Đăng ký ViewSet với router
router.register(r'room', RoomViewSet)
router.register(r'user', UserViewSet)
router.register(r'utilities', UtilitiesViewSet)
router.register(r'area', AreaViewSet)
router.register(r'login', LoginViewSet, basename='login')
router.register(r'slider', SliderViewSet)
router.register(r'cart', CartViewSet)
router.register(r'order', OrderViewSet)
router.register(r'orderDetails', OrderDetailViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'vouchers', VoucherViewSet)
router.register(r'search', SearchViewSet, basename='search')

urlpatterns = [
    path('', include(router.urls)),  # Bao gồm các URL từ router
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # zalo pay
    path("zalopay/create-order/", CreateOrderZaloPayView.as_view(), name="create-zalopay-order"),
    path("zalopay/payment-order/", CheckoutZaloPayView.as_view(), name="payment-order"),
    path('zalopay-callback/', ZaloPayCallback.as_view(), name='zalopay-callback'),
    path('zalopay-order-status/', ZaloPayOrderStatus.as_view(), name='zalopay-order-status'),

    # path('vnpay/', include('vnpay.api_urls')),
    # path('login/', LoginViewSet.as_view(), name='login'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
