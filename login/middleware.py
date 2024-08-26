from django.shortcuts import redirect
from django.contrib import messages
from django.urls import reverse

class SessionExpiryMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated and not request.session.exists(request.session.session_key):
            messages.info(request, "Please login.")
            return redirect(reverse('custom_login'))
        
        response = self.get_response(request)
        return response
