from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.contrib.auth.models import User, Group
from superuser.forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.http import Http404
from django.contrib import messages  # Import messages


# Create your views here.

class ListParkingUserView(ListView):
    model = User
    template_name = 'list_parking_user.html'
    context_object_name = 'parking'
    
    def get_queryset(self):
        # Get the "Admin" group
        admin_group = Group.objects.get(name="Parking")
        # Filter users who belong to the "Admin" group
        return User.objects.filter(groups=admin_group)


class DetailParkingUserView(DetailView):
    model = User
    template_name = 'detail_parking_user.html'
    context_object_name = 'parking'

    def get_object(self, queryset=None):
        # Get the user object based on the pk (primary key)
        user = super().get_object(queryset)

        # Ensure the user belongs to the "Parking" group
        engineer_group = Group.objects.get(name="Parking")
        if not user.groups.filter(name=engineer_group.name).exists():
            raise Http404("This user is not Parking User.")
        
        return user


class UpdateParkingUserView(UpdateView):
    model = User
    template_name = 'create_admin.html'  # Reuse the same template
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('list_parking_user')

    def form_valid(self, form):
        response = super().form_valid(form)
        # If the group is changed, update the user's group
        selected_group = form.cleaned_data['group']
        self.object.groups.clear()  # Remove existing groups
        self.object.groups.add(selected_group)  # Add the new group
        
        # Add success message
        messages.success(self.request, "Parking User updated successfully!")
        
        return response

    def get_success_url(self):
        return reverse_lazy('detail_parking_user', kwargs={'pk': self.object.pk})


class DeleteParkingUserView(DeleteView):
    model = User
    template_name = 'delete_parking_user.html'  # This will be the confirmation template
    context_object_name = 'parking'
    success_url = reverse_lazy('list_parking_user')  # Redirect after successful deletion

    def delete(self, request, *args, **kwargs):
        user = self.get_object()
        # Add success message
        messages.success(request, f"Parking User {user.username} deleted successfully!")
        return super().delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        user = super().get_object(queryset)
        # Ensure the user belongs to the "Parking" group
        engineer_group = Group.objects.get(name="Parking")
        if not user.groups.filter(name=engineer_group.name).exists():
            raise Http404("This user is not a parking user.")
        return user
