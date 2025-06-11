from rest_framework import generics
from .models import User
from .serializers import UserSerializer

#This view uses Django REST Framework's `CreateAPIView` to expose the `register` endpoint (`/api/users/register/`) for signing up users.
# No authentication is required for this view.

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer