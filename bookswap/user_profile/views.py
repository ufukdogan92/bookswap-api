# Create your views here.
from itertools import chain
from django.db.models import Q
from rest_framework import viewsets, mixins, generics
from django.contrib.auth.models import User
from .models import UserProfile
from .serializers import UserProfileSerializer,UserSerializer,GlobalSearchSerializer

class UserProfileViewSet(viewsets.ModelViewSet):  
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class UserViewSet(viewsets.ModelViewSet):  
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GlobalSearchList(generics.ListAPIView):
    serializer_class = GlobalSearchSerializer

    def get_queryset(self):
        query = self.request.query_params.get('query', None)   

        user = User.objects.filter(
            username = query,
        )

        all_results = list(chain(user))
        return all_results