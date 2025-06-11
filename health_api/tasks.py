from celery import shared_task
from django.core.mail import send_mail
from .models import HealthRecord

# This background task sends the notification email in a non-blocking way using Celery.
def notify_email_text(patient_name):
    return f"You’ve been assigned to a new patient: {patient_name}"

@shared_task
def notify_doctor_async(record_id):
    try:
        record = HealthRecord.objects.get(id=record_id)
        if record.doctor and record.doctor.email:
            send_mail(
                subject='New Patient Assigned',
                message=notify_email_text(record.patient.username),
                from_email='noreply@healthapi.com',
                recipient_list=[record.doctor.email],
            )
            return 'Success'
    except HealthRecord.DoesNotExist:
        return 'Record not found'
    return 'Doctor not assigned'