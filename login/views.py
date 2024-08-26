from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required

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
            else:
                return redirect('default_dashboard')
        else:
            # Invalid credentials
            return render(request, 'login.html', {'error': 'Invalid credentials'})

    return render(request, 'login.html')

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