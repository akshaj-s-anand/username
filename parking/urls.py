from django.urls import path
from parking.views import ListParkingUserView, DetailParkingUserView, UpdateParkingUserView, DeleteParkingUserView

urlpatterns = [
    path('parking-users/', ListParkingUserView.as_view(), name='list_parking_user'),  # List view of parking users
    path('parking-user/<int:pk>/', DetailParkingUserView.as_view(), name='detail_parking_user'),  # Detail view for specific user
    path('parking-user/<int:pk>/edit/', UpdateParkingUserView.as_view(), name='edit_parking_user'),  # Edit view for specific user
    path('parking-user/<int:pk>/delete/', DeleteParkingUserView.as_view(), name='delete_parking_user'),  # Delete confirmation view
]
