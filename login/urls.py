from django.urls import path
from .views import custom_login, user_dashboard_view, admin_dashboard_view, custom_logout, superuser_dashboard_view

urlpatterns = [
    path('', custom_login, name='custom_login'),
    path('logout/', custom_logout, name='custom_logout'),
    path('user/<int:pk>/', user_dashboard_view, name='user_dashboard'),
    path('admin/<int:pk>/', admin_dashboard_view, name='admin_dashboard'),
    path('superuser_dashboard/<int:pk>/', superuser_dashboard_view, name='superuser_dashboard'),
]