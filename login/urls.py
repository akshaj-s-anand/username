from django.urls import path
from .views import custom_login, custom_logout, SuperuserDashboardView

urlpatterns = [
    path('', custom_login, name='custom_login'),
    path('logout/', custom_logout, name='custom_logout'),
    # path('user/<int:pk>/', user_dashboard_view, name='user_dashboard'),
    # path('admin/<int:pk>/', admin_dashboard_view, name='admin_dashboard'),
    path('superuser-dashboard/', SuperuserDashboardView.as_view(), name='superuser_dashboard'),
]