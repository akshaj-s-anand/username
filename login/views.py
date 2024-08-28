from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import DetailView
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied

def custom_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if user.groups.filter(name='User').exists():
                return redirect('user_dashboard', pk=user.pk)
            elif user.groups.filter(name='Admin').exists():
                return redirect('admin_dashboard', pk=user.pk)
            elif user.is_superuser:
                return redirect('superuser_dashboard')
            else:
                return redirect('login')
        else:
            # Invalid credentials
            return render(request, 'login.html', {'error': 'Invalid credentials'})

    return render(request, 'login.html')

class SuperuserDashboardView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = User
    template_name = 'superuser_dashboard.html'
    context_object_name = 'superuser'

    def get_object(self, queryset=None):
        # Return the current logged-in user's profile
        return self.request.user

    def test_func(self):
        # Check if the logged-in user is a superuser
        return self.request.user.is_superuser

    def handle_no_permission(self):
        # Redirect non-superusers to a different page or raise a PermissionDenied error
        raise PermissionDenied("You do not have permission to access this page.")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add any additional context data here
        return context

@login_required
def user_dashboard_view(request, pk):
    # Add logic specific to user dashboard
    return render(request, 'user_dashboard.html', {'user_id': pk})


@login_required
def admin_dashboard_view(request, pk):
    # Add logic specific to admin dashboard
    return render(request, 'admin_dashboard.html', {'admin_id': pk})


@login_required
def custom_logout(request):
    request.session.flush()
    logout(request)
    return render(request,'login.html')