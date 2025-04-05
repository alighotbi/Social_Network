from rest_framework import generics

from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

from .serializers import RegisterSerializer

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer 
    
    
