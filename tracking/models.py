from django.db import models

# Create your models here.
class DeviceLocation(models.Model):
    device_id = models.CharField(max_length=50)   # mobile or future bus ID
    latitude = models.FloatField()
    longitude = models.FloatField()
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.device_id} @ {self.latitude}, {self.longitude}"