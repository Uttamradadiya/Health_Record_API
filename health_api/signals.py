from django.db.models.signals import post_save
from django.dispatch import receiver
from health_api.models import HealthRecord
from health_api.tasks import notify_doctor_async

@receiver(post_save, sender=HealthRecord)
def notify_doctor(sender, instance, created, **kwargs):
    if created and instance.doctor:
        notify_doctor_async.delay(instance.id)  # Non-blocking async task