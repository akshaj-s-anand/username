from django.shortcuts import render, redirect
from django.views.generic import View, CreateView, ListView, UpdateView, DetailView, DeleteView, TemplateView
from django.contrib.auth.models import User, Group
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from superuser.forms import CustomUserCreationForm
from django.http import Http404
# Create your views here.


class ProfileView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'profile.html'
    context_object_name = 'profile'

    def get_object(self, queryset=None):
        # Return the current logged-in user's profile
        return self.request.user
    
class ProfileEdit(LoginRequiredMixin, UpdateView):
    model = User
    fields = ['username', 'email', 'first_name', 'last_name']
    template_name = 'profile_edit.html'
    context_object_name = 'profile'

    def get_object(self, queryset=None):
        # Return the current logged-in user's profile
        return self.request.user

    def get_success_url(self):
        # Redirect the user back to their profile page after successfully editing their profile
        return reverse_lazy('profile')
    
class PasswordEditView(LoginRequiredMixin, PasswordChangeView):
    template_name = 'password_change.html'
    success_url = reverse_lazy('profile')  # Redirect to the profile page after password change

    def form_valid(self, form):
        messages.success(self.request, "Your password was successfully updated!")
        return super().form_valid(form)
    

class CreateAdminView(CreateView):
    model = User
    form_class = CustomUserCreationForm
    template_name = 'create_admin.html'
    success_url = reverse_lazy('profile')  # Adjust as necessary

    def form_valid(self, form):
        # Save the form and create the user
        response = super().form_valid(form)
        
        # Assign the user to the group selected in the form
        selected_group = form.cleaned_data['group']
        self.object.groups.add(selected_group)
        
        return response

class ListAdminView(ListView):
    model = User
    template_name = 'list_admin.html'
    context_object_name = 'engineers'
    
    def get_queryset(self):
        # Get the "Admin" group
        admin_group = Group.objects.get(name="Engineer")
        # Filter users who belong to the "Admin" group
        return User.objects.filter(groups=admin_group)
    
class DetailAdminView(DetailView):
    model = User
    template_name = 'detail_admin.html'
    context_object_name = 'engineer'

    def get_object(self, queryset=None):
        # Get the user object based on the pk (primary key)
        user = super().get_object(queryset)

        # Ensure the user belongs to the "Engineer" group
        engineer_group = Group.objects.get(name="Engineer")
        if not user.groups.filter(name=engineer_group.name).exists():
            raise Http404("This user is not an Engineer.")
        
        return user
    
class UpdateAdminView(UpdateView):
    model = User
    template_name = 'create_admin.html'  # Reuse the same template
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('list_admin')

    def form_valid(self, form):
        response = super().form_valid(form)
        # If the group is changed, update the user's group
        selected_group = form.cleaned_data['group']
        self.object.groups.clear()  # Remove existing groups
        self.object.groups.add(selected_group)  # Add the new group
        return response

    def get_success_url(self):
        return reverse_lazy('detail_admin', kwargs={'pk': self.object.pk})
    
    
class DeleteAdminView(DeleteView):
    model = User
    template_name = 'delete_admin.html'  # This will be the confirmation template
    context_object_name = 'engineer'
    success_url = reverse_lazy('list_admin')  # Redirect after successful deletion

    def get_object(self, queryset=None):
        user = super().get_object(queryset)
        # Ensure the user belongs to the "Engineer" group
        engineer_group = Group.objects.get(name="Engineer")
        if not user.groups.filter(name=engineer_group.name).exists():
            raise Http404("This user is not an Engineer.")
        return user