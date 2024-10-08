# your_app/templatetags/custom_filters.py

from django import template
from django.contrib.auth.models import Group

register = template.Library()

@register.filter
def is_group(user, group_name):
    return user.groups.filter(name=group_name).exists()
