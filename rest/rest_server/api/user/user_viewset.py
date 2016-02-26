"""
The viewset for the register
"""

"""
imports
"""

from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model
from user_serializer import UserSerializer

"""
viewset
"""

class UserRegisterView(CreateAPIView):
    model = get_user_model()
    serializer_class = UserSerializer
