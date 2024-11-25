from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from e_be_booking_hotel.models import Room
from e_be_booking_hotel.serializers import RoomSerializer


class SearchViewSet(viewsets.ViewSet):
    @swagger_auto_schema(
        operation_summary="Search Rooms",
        operation_description="Search for rooms by name, price, and availability.",
        manual_parameters=[
            openapi.Parameter(
                'name', openapi.IN_QUERY,
                description="Search by room name",
                type=openapi.TYPE_STRING
            ),
            openapi.Parameter(
                'price', openapi.IN_QUERY,
                description="Maximum price of the room",
                type=openapi.TYPE_NUMBER
            )
        ],
        responses={
            200: "A list of rooms matching the search criteria",
            400: "Invalid input parameters"
        }
    )
    def list(self, request):
        # Lấy tất cả các phòng
        queryset = Room.objects.all()

        # Lấy các tham số tìm kiếm từ request
        name = request.query_params.get('name')
        price = request.query_params.get('price')

        # Tìm kiếm theo tên phòng
        if name:
            queryset = queryset.filter(room_type__icontains=name)

        # Tìm kiếm theo giá
        if price:
            try:
                price = float(price)  # Chuyển đổi giá trị sang float
                queryset = queryset.filter(price_per_night__lte=price)  # Tìm kiếm phòng có giá nhỏ hơn hoặc bằng
            except ValueError:
                return Response({"error": "Invalid price value"}, status=status.HTTP_400_BAD_REQUEST)

        # Serialize dữ liệu và trả về phản hồi
        serializer = RoomSerializer(queryset, many=True)
        return Response(serializer.data)
