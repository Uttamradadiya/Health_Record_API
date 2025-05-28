from rest_framework import permissions

class IsPatientOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.patient == request.user

class IsAssignedDoctor(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.doctor == request.user