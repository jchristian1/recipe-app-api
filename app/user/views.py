"""
Views from the user API.
"""
from rest_framework import generics

from user.serializers import UserSerializers

class CreateUserView(generic.CreateAPIView):
    """Create a new user in the system"""
    serializer_class = UserSerializers

