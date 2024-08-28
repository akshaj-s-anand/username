from django.urls import path
from superuser.views import ProfileView, ProfileEdit, PasswordEditView

urlpatterns = [
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/edit/', ProfileEdit.as_view(), name='profile_edit'),
    path('profile/change-password/', PasswordEditView.as_view(), name='change_password'),
]