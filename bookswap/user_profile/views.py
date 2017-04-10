# Create your views here.
from itertools import chain
from django.db.models import Q
from rest_framework import viewsets, mixins, generics
from django.contrib.auth.models import User
from .models import UserProfile
from .serializers import UserProfileSerializer,UserSerializer,GlobalSearchSerializer,UserSearchSerializer

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

class UserSearchList(generics.ListAPIView):
    serializer_class = UserSearchSerializer

    def get_queryset(self):
        query = self.request.query_params.get('query', None)
        qs = query.split(" ")
        user = User.objects.filter(
            Q(first_name__icontains=qs[0]) | Q(last_name__icontains=qs[1])
        )

        all_results = list(chain(user))
        return all_results