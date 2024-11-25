from .hotel import HotelSerializer
from .user import UserSerializer
from .room import RoomSerializer
from .utilities import UtilitiesSerializer
from .room_utilities import RoomUtilitiesSerializer
from .area import AreaSerializer
from .login import LoginSerializer
from .slider import SliderSerializer
from .cart import CartSerializer
from .order import OrderSerializer
from .order_detail import OrderDetailSerializer
from .review import ReviewSerializer
from .voucher import VoucherSerializer

# zalopay
from .zalopay import ZalopayOrderSerializer
from .zalopay import ZalopayCallbackSerializer
from .zalopay import ZaloPayCreateOrderRequestSerializer