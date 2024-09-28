from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import DetailView
from django.contrib.auth.models import User
from django.contrib.admin.models import LogEntry
from django.core.exceptions import PermissionDenied

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import Group

def custom_login(request):
    if request.user.is_authenticated:
        return redirect('superuser_dashboard')  # Redirect to a unified dashboard

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('superuser_dashboard')  # Redirect all users to the unified dashboard
        else:
            # Invalid credentials
            return render(request, 'login.html', {'error': 'Invalid credentials'})

    return render(request, 'login.html')

class SuperuserDashboardView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'superuser_dashboard.html'
    context_object_name = 'user'

    def get_object(self, queryset=None):
        # Return the current logged-in user
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Retrieve recent actions by the current user (can be any user)
        recent_actions = LogEntry.objects.filter(user=self.request.user).order_by('-action_time')[:10]
        context['recent_actions'] = recent_actions
        return context

# @login_required
# def user_dashboard_view(request, pk):
#     # Add logic specific to user dashboard
#     return render(request, 'user_dashboard.html', {'user_id': pk})


# @login_required
# def admin_dashboard_view(request, pk):
#     # Add logic specific to admin dashboard
#     return render(request, 'admin_dashboard.html', {'admin_id': pk})


@login_required
def custom_logout(request):
    request.session.flush()
    logout(request)
    return render(request,'login.html')