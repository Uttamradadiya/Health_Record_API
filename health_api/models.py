from django.db import models
from users.models import User

# This model represents a health record. It has a `patient` (record owner), an optional `doctor` (assigned doctor), and some content fields. 
# It's automatically timestamped.

class HealthRecord(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name="records")
    doctor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, limit_choices_to={'role': 'DOCTOR'})
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

# This model allows doctors to comment on patient records, but only if they are the assigned doctor.

class Comment(models.Model):
    record = models.ForeignKey(HealthRecord, on_delete=models.CASCADE, related_name="comments")
    doctor = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)