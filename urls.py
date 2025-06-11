# urls.py (root)
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# JWT token endpoints + modular routing for users and records.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('health_api.urls')),       # ✅ required
    path('api/users/', include('users.urls')),      # ✅ user registration
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]