from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .models import HealthRecord, Comment
from .serializers import HealthRecordSerializer, CommentSerializer
from .permissions import IsPatientOwner, IsAssignedDoctor

class HealthRecordViewSet(viewsets.ModelViewSet):
    queryset = HealthRecord.objects.all()
    serializer_class = HealthRecordSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'PATIENT':
            return HealthRecord.objects.filter(patient=user)
        elif user.role == 'DOCTOR':
            return HealthRecord.objects.filter(doctor=user)
        return HealthRecord.objects.none()

    def create(self, request, *args, **kwargs):
        # 🔐 Only patients can create records
        if request.user.role != 'PATIENT':
            return Response(
                {'detail': 'Only patients can create health records.'},
                status=status.HTTP_403_FORBIDDEN
            )
        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(patient=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Comment.objects.filter(doctor=self.request.user)

    def perform_create(self, serializer):
        record = serializer.validated_data['record']
        if record.doctor != self.request.user:
            raise PermissionError("You are not assigned to this record.")
        serializer.save(doctor=self.request.user)