from django.db import models
from django.contrib.auth.models import User

class DetectionLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    object_name = models.CharField(max_length=100)
    confidence = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f"{self.object_name} ({self.confidence:.2f}) at {self.timestamp}"