from rest_framework.test import APITestCase
from users.models import User
from health_api.models import HealthRecord
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.urls import reverse

class HealthRecordTestCase(APITestCase):

    # Set up two users: one patient and one doctor
    def setUp(self):
        self.patient = User.objects.create_user(username='abc', password='abcd123', role='PATIENT')
        self.doctor = User.objects.create_user(username='xyz', password='xyz@1234', role='DOCTOR')
        self.token = str(RefreshToken.for_user(self.patient).access_token)
        self.auth_header = f"Bearer {self.token}"

    # Test that patient can create a health record
    def test_patient_can_create_record(self):
        self.client.credentials(HTTP_AUTHORIZATION=self.auth_header)
        url = reverse('healthrecord-list')  # Dynamically resolves '/api/records/'
        response = self.client.post(url, {
            'title': 'Test Record',
            'content': 'Test Content',
            'doctor': self.doctor.id
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # Test that a doctor should not be able to create a record
    def test_doctor_cannot_create_record(self):
        token = str(RefreshToken.for_user(self.doctor).access_token)
        
        # Set doctor token in headers
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
        url = reverse('healthrecord-list')
        response = self.client.post(url, {
            'title': 'Should Fail',
            'content': 'Blocked',
            'doctor': self.doctor.id
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)