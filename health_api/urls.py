from django.urls import path, include
from rest_framework.routers import DefaultRouter
from health_api.views import HealthRecordViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'records', HealthRecordViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls))
]