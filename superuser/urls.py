from django.urls import path
from superuser.views import ProfileView, ProfileEdit, PasswordEditView, CreateAdminView, ListAdminView, DetailAdminView, UpdateAdminView, DeleteAdminView

urlpatterns = [
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/edit/', ProfileEdit.as_view(), name='profile_edit'),
    path('profile/change-password/', PasswordEditView.as_view(), name='change_password'),
    path('create-user/', CreateAdminView.as_view(), name='create_admin'),
    path('list-engineer/', ListAdminView.as_view(), name='list_admin'),
    path('engineer/<int:pk>/', DetailAdminView.as_view(), name='detail_admin'),
    path('engineer/<int:pk>/edit/', UpdateAdminView.as_view(), name='edit_admin'),
    path('engineer/<int:pk>/delete/', DeleteAdminView.as_view(), name='delete_admin'),
]