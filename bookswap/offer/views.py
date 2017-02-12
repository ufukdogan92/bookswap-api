from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .models import Offer
from .serializers import OfferSerializer

class OfferViewSet(viewsets.ModelViewSet): 
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer

