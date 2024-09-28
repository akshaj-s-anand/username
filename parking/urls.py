from django.urls import path
from parking.views import ListParkingUserView, DetailParkingUserView, UpdateParkingUserView, DeleteParkingUserView, VehicleTypeView, ListVehicleTypeView, DetailVehicleTypeView, VehicleTypeUpdateView, VehicleTypeDeleteView

urlpatterns = [
    path('parking-users/', ListParkingUserView.as_view(), name='list_parking_user'),  # List view of parking users
    path('parking-user/<int:pk>/', DetailParkingUserView.as_view(), name='detail_parking_user'),  # Detail view for specific user
    path('parking-user/<int:pk>/edit/', UpdateParkingUserView.as_view(), name='edit_parking_user'),  # Edit view for specific user
    path('parking-user/<int:pk>/delete/', DeleteParkingUserView.as_view(), name='delete_parking_user'),  # Delete confirmation view
    path('vehicle-type/create/', VehicleTypeView.as_view(), name='vehicle_create'),
    path('vehicle-type/', ListVehicleTypeView.as_view(), name='vehicle_list'),
    path('vehicle-type/<int:pk>/', DetailVehicleTypeView.as_view(), name='vehicle_list_details'),
    path('vehicle-type/update/<int:pk>/', VehicleTypeUpdateView.as_view(), name='vehicle_update'),
    path('vehicle-type/delete/<int:pk>/', VehicleTypeDeleteView.as_view(), name='delete_vehicle_type'),

]
