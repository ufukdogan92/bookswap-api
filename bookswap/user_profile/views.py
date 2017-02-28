# Create your views here.
from rest_framework import viewsets 
from django.contrib.auth.models import User
from .models import UserProfile
from .serializers import UserProfileSerializer,UserSerializer

class UserProfileViewSet(viewsets.ModelViewSet):  
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class UserViewSet(viewsets.ModelViewSet):  
    queryset = User.objects.all()
    serializer_class = UserSerializer