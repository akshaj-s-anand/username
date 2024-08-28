from django.shortcuts import render
from django.views.generic import View, CreateView, ListView, UpdateView, DetailView, DeleteView, TemplateView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from django.contrib import messages
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