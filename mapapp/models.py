# models.py
from django.db import models

class Marker(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    event_type = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='markers/', blank=True, null=True)
    video = models.FileField(upload_to='videos/', blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    is_permanent = models.BooleanField(default=False)

    def __str__(self):
        return self.title
