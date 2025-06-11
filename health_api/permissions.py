from rest_framework import permissions

# These permissions ensure access is controlled:
# `IsPatientOwner` ensures a patient can only see/update their own records.
# `IsAssignedDoctor` allows access only to assigned doctors.

class IsPatientOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.patient == request.user

class IsAssignedDoctor(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.doctor == request.user