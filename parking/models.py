from django.db import models
from django.utils import timezone

class VehicleType(models.Model):
    vehicle_type = models.CharField(max_length=50)
    fair = models.IntegerField()

class VehicleInfo(models.Model):
    vehicle_number = models.CharField(max_length=12)
    vehicle_type = models.ForeignKey(VehicleType, on_delete=models.CASCADE)
    owner_name = models.CharField(max_length=50, blank=True, null=True)
    time_in = models.DateTimeField(default=timezone.now)
    time_out = models.DateTimeField(default=timezone.now)
    vehicle_out = models.BooleanField()
    
    
